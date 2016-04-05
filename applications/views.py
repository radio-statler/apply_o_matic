from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import FormView

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
