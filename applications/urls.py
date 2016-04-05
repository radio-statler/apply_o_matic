from django.conf.urls import patterns, include, url

import applications.views

urlpatterns = patterns('', url(r'^$', applications.views.CreateApplicationView.as_view(), name="application-submit"))