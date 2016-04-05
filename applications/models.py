from __future__ import unicode_literals

from django.db import models
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType
from phonenumber_field.modelfields import PhoneNumberField

from .choices import *

# Create your models here.
class Application(models.Model):
    name = models.CharField(verbose_name="Name/Handle",
                            help_text="Give us your name, handle, or alternate identifying mark",
                            error_messages={'required': 'Please enter your name/handle' },
                            max_length=25)
    email_address = models.EmailField(verbose_name="E-Mail",
                                      help_text="Give us an e-mail address we can use to get in touch with you",
                                      error_messages={'required': 'Please enter a valid e-mail address' })
    phone_number = PhoneNumberField(verbose_name="Phone Number",
                                           help_text="Give us a phone number to reach you at",
                                           blank=True)
    show_name = models.CharField(max_length=45,
                                 verbose_name="Show Name",
                                 help_text="A short, catchy title for your show",
                                 error_messages={'required': 'Your show must have a name.  You can change it later'})
    show_type = models.IntegerField(verbose_name="Show Type",
                                    help_text="What type of show do you want to air",
                                    choices=SHOW_TYPE_CHOICES)
    show_description = models.TextField(verbose_name="Description",
                                        help_text="Briefly describe the format and content of your show",
                                        error_messages={'required': 'You must submit a description' })
    primary_preferred_day = models.CharField(max_length=8,
                                             verbose_name="Preferred Day",
                                             help_text="Which day would you prefer your show on",
                                             error_messages={'required': 'Please choose a preferred day and time' },
                                             choices=PREFERRED_DAY_CHOICES)
    primary_preferred_time = models.CharField(max_length=15,
                                              verbose_name="Preferred Time",
                                              help_text="What time of day would you prefer",
                                              error_messages={'required': 'Please choose a preferred day and time' },
                                              choices=PREFERRED_TIME_CHOICES)
    backup_preferred_day = models.CharField(max_length=8,
                                            verbose_name="2nd Preferred Day",
                                            help_text="Which day would you prefer your show on",
                                            choices=PREFERRED_DAY_CHOICES,
                                            blank=True)
    backup_preferred_time = models.CharField(max_length=15,
                                             verbose_name="2nd Preferred Time",
                                             help_text="What time of day would you prefer",
                                             choices=PREFERRED_TIME_CHOICES,
                                             blank=True)
    contact_via_sms = models.BooleanField(default=False,
                                          verbose_name="Contact me about my show via SMS")
    volunteer_interest = models.BooleanField(default=False,
                                             verbose_name="I'm interested in volunteering to help")

    @property
    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model),
                                    args=(self.id,))