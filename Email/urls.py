from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from Email import views

urlpatterns = [
    url(r'test', views.test_server),
    url(r'post', views.incoming_webhook),
    url(r'email', views.send_email),
]

