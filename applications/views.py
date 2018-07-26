from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic import TemplateView

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from sparkpost import SparkPost
from slackclient import SlackClient


from .forms import ApplicationForm

class CreateApplicationView(FormView):
    form_class = ApplicationForm
    template_name = 'index.html'
    fields = ['name',
              'email_address',
              'phone_number',
              'show_name',
              'show_type',
              'show_description',
              'primary_preferred_day',
              'primary_preferred_time',
              'backup_preferred_day',
              'backup_preferred_time',
              'contact_via_sms',
              'volunteer_interest']
    success_url = reverse_lazy('submission-success')

    def form_valid(self, form):
        application = form.save()
        current_site = get_current_site(self.request)
        email = SparkPost(settings.SPARKPOST_API_KEY)
        slack = SlackClient(settings.SLACK_TOKEN)

        sub_data = {
            'name': form.cleaned_data['name'],
            'submitter_email': form.cleaned_data['email_address'],
            'phone_number': str(form.cleaned_data['phone_number']),
            'show_name': form.cleaned_data['show_name'],
            'show_type': form.cleaned_data['show_type'],
            'show_description': form.cleaned_data['show_description'],
            'pri_preferred_day': form.cleaned_data['primary_preferred_day'],
            'pri_preferred_time': form.cleaned_data['primary_preferred_time'],
            'url': 'https://%s%s' % (current_site.domain, application.get_admin_url)
        }
        if form.cleaned_data['volunteer_interest']:
            sub_data['volunteering'] = 'yes'
        if form.cleaned_data['contact_via_sms']:
            sub_data['sms'] = 'yes'
        if form.cleaned_data['backup_preferred_day']:
            sub_data['bck_preferred_day'] = form.cleaned_data['backup_preferred_day']
        if form.cleaned_data['backup_preferred_time']:
            sub_data['bck_preferred_time'] = form.cleaned_data['backup_preferred_time']

        email.transmissions.send(
            recipients=[form.cleaned_data['email_address']],
            template='radio-statler-submission-acknowledge',
            substitution_data=sub_data

        )
        email.transmissions.send(
            recipient_list='rs-notification-list',
            template='radio-statler-show-application-notification',
            substitution_data=sub_data
        )
        slack.api_call(
            'chat.postMessage',
            channel=settings.SLACK_CHANNEL,
            text='New Show Application: <%s|%s> from %s &lt;%s&gt;' % (sub_data['url'], sub_data['show_name'], sub_data['name'], sub_data['submitter_email']),
            username=settings.SLACK_USERNAME
        )
        return super(CreateApplicationView, self).form_valid(form)

class SubmissionSuccessView(TemplateView):
    template_name = 'success.html'