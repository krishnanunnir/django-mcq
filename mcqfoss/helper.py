from django.shortcuts import render
from exam.models import *
from django.http import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout
from authentication.models import *

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
