from django.contrib import admin

# Register your models here.
from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('show_name','name','email_address','phone_number','show_type','primary_preferred_day','primary_preferred_time')

admin.site.register(Application, ApplicationAdmin)