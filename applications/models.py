from __future__ import unicode_literals

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .choices import *

# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=25,
                                 label="Name/Handle",
                                 help_text="Give us your name, handle, or alternate identifying mark",
                                 error_messages="Please enter your name/handle")
    email_address = models.EmailField(label="E-Mail",
                                      help_text="Give us an e-mail address we can use to get in touch with you",
                                      error_messages="Please enter a valid e-mail address")
    phone_number = models.PhoneNumberField(label="Phone Number",
                                           help_text="Give us a phone number to reach you at",
                                           required=False)
    show_type = models.IntegerField(label="Show Type",
                                    help_text="What type of show do you want to air",
                                    choices=SHOW_TYPE_CHOICES)
    show_description = models.TextField(label="Description",
                                        help_text="Briefly describe the format and content of your show",
                                        error_messages="You must submit a description")
    primary_preferred_day = models.CharField(max_length=8,
                                             label="Preferred Day",
                                             help_text="Which day would you prefer your show on",
                                             error_messages="Please choose a preferred day and time",
                                             choices=PREFERRED_DAY_CHOICES)
    primary_preferred_time = models.CharField(max_length=15,
                                              label="Preferred Time",
                                              help_text="What time of day would you prefer",
                                              error_messages="Please choose a preferred day and time",
                                              choices=PREFERRED_TIME_CHOICES)
    backup_preferred_day = models.CharField(max_length=8,
                                            label="2nd Preferred Day",
                                            help_text="Which day would you prefer your show on",
                                            choices=PREFERRED_DAY_CHOICES,
                                            required=False)
    backup_preferred_time = models.CharField(max_length=15,
                                             label="2nd Preferred Time",
                                             help_text="What time of day would you prefer",
                                             choices=PREFERRED_TIME_CHOICES,
                                             required=False)
    contact_via_sms = models.BooleanField(default=False,
                                          label="Contact me about my show via SMS")
    volunteer_interest = models.BooleanField(default=False,
                                             label="I'm interested in volunteering to help")