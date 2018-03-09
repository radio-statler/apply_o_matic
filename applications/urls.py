from django.conf.urls import *

import applications.views

urlpatterns = [
    url(r'^$', applications.views.CreateApplicationView.as_view(), name='application-submit'),
    url(r'^success/', applications.views.SubmissionSuccessView.as_view(), name='submission-success')
]
