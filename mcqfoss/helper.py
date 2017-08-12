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

def check_valid(start_time,end_time,date):
    if  date_check( date ) == 1 or date_check( date ) == -1:
        return "The test is set for %s" % date
    else:
        if time_check( start_time ) == 1 and time_check( end_time ) == -1:
            return None
        else:
            return "The test is not accessible as it is set for %s to %s" % (start_time,end_time)
def cleaned_post(post_item):
    answer_values={}
    for question_no,radio_answer in post_item.items():
        if 'csrf' in question_no:
            continue
        else:
            answer_values[question_no]=radio_answer
    return answer_values