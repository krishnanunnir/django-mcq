from django.shortcuts import render
from exam.models import *
from django.http import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout
from authentication.models import *
import datetime

def test_authentication(username,test):
    try:
        user = Student.objects.get( user__username = username )
        test_items = Test.objects.get( test_title = test )
        if test_items.permitted_for == user.department:
            return True
        else:
            return False
    except:
        return False


def now_time():
    return datetime.datetime.time(datetime.datetime.now())

def now_date():
    return datetime.datetime.date(datetime.datetime.now())

def time_check( time_point ):
    if now_time() < time_point:
        return -1
    elif now_time() > time_point:
        return 1
    else:
        return 0


def date_check( date_point ):
    if now_date() < date_point:
        return -1
    elif now_date() > date_point:
        return 1
    else:
        return 0
