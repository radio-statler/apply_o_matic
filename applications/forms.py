from django.forms import ModelForm
from django.forms.widgets import TextInput, EmailInput, Select, Textarea, CheckboxInput

from .models import Application

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
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
        widgets = {
            'name':TextInput(attrs={'class':'field text medium'}),
            'email_address':EmailInput(attrs={'class':'field text medium'}),
            'phone_number':TextInput(attrs={'class':'field text medium'}),
            'show_name':TextInput(attrs={'class':'field text large'}),
            'show_type':Select(attrs={'class':'field select medium'}),
            'show_description':Textarea(attrs={'class':'field textarea large'}),
            'primary_preferred_day':Select(attrs={'class':'field select medium'}),
            'primary_preferred_time':Select(attrs={'class':'field select medium'}),
            'backup_preferred_day':Select(attrs={'class':'field select medium'}),
            'backup_preferred_time':Select(attrs={'class':'field select medium'}),
            'contact_via_sms':CheckboxInput(attrs={'class':'field checkbox'}),
            'volunteer_interest':CheckboxInput(attrs={'class':'field checkbox'})
        }