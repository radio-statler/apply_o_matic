from django.views.generic import FormView

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from sparkpost import SparkPost

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
    success_url = 'https://www.google.com'

    def form_valid(self, form):
        application = form.save()
        current_site = get_current_site()
        email = SparkPost(settings.SPARKPOST_API_KEY)
        sub_data = {
            'name': form.cleaned_data['name'],
            'email': form.cleaned_data['email_address'],
            'phone_number': form.cleaned_data['phone_number'],
            'show_name': form.cleaned_data['show_name'],
            'show_type': form.cleaned_data['show_type'],
            'show_description': form.cleaned_data['show_description'],
            'pri_preferred_day': form.cleaned_data['primary_preferred_day'],
            'pri_preferred_time': form.cleaned_data['primary_preferred_time'],
            'url': 'https://%s%s' % (current_site.domain, application.get_admin_url)
        }
        if form.cleaned_data['volunteer_interest']:
            sub_data['volunteer_interest'] = 'yes'
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
        return super(CreateApplicationView, self).form_valid(form)

