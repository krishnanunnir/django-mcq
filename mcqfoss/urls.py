"""mcqfoss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mcqfoss.views import *
from exam.views import *
from authentication.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$',home),
    url(r'^login/$',log_in),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^currenttime/(\d+)/$',current_time),
    url(r'^tests/(\w+)/$',test_display),
    url(r'^signup/$',signup),
    url(r'^logout/$',logout_view),
    url(r'^current_user/$',current_user),
    url(r'^score/(\w+)/$',display_scores),
]
