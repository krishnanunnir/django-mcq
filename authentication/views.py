from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User
from exam.models import *
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login,logout
import re
from mcqfoss.helper import *
pattern = re.compile("TVE\d{2}\w{2}\d{3}")
# Create your views here.

def signup( request ):
    error =[]
    form = StudentForm()
    form_department= StudentDepartmentForm()    
    if request.method == "POST":
        post_values = request.POST
        if not post_values['password'] == post_values["password_confirm"]:
            error.append("Password and Confirm Password doesn't match.")
        if not pattern.match(post_values['username']):
            error.append("Enter your roll number as your username")
        if User.objects.filter(email=post_values["email"]):
            error.append("Email already exists")
        if not error:
            try:
                user_object = User.objects.create_user(username = post_values['username'],email = post_values['email'], password = post_values['password'],first_name = post_values['first_name'],last_name = post_values['last_name'])
                user_object.save()
                dept=Department.objects.get(id=post_values['department'])
                student_dept =Student.objects.create(user =user_object,department=dept)
                student_dept.save()
                return HttpResponse("Successful")
            except:
                error.append("An error occured during signup.")

    return render(request,'sign_up.html',{'form':form,'form_department':form_department,'error':error})


def log_in(request):
    if  not request.user.is_authenticated():
        form = Login()
        error = []
        if request.method == "POST":
            post_value = request.POST
            username = post_value['username']
            password = post_value['password']
            user = authenticate(username = username,password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/current_user')
                else:
                    error.append("User account is disabled")
            else:
                error.append("Invalid username or password")
            return render(request,'login.html',{'form':form,'error':error})
        else:
            return render(request,'login.html',{'form':form,'error':error})
    else:
        return redirect('/current_user')

def current_user(request):
    upcoming=[]
    ongoing=[]
    unattended=[]
    completed={}
    maximum_score={}
    if request.user.is_authenticated():
        user = request.user
        student = Student.objects.get( user__username = user.username )
        test_items = Test.objects.filter( permitted_for = student.department  )
        for test_check in test_items:
            test_bit=check_finished( test_check.start_time,test_check.end_time,test_check.date_of_exam )
            if test_bit==-1:
                upcoming.append(test_check.test_title)
            elif test_bit==1:
                try:
                    test_score_item=Testscore.objects.get(test=test_check,student=student)
                    completed[test_check.test_title]=test_score_item.test_score
                    maximum_score[test_check.test_title]=test_check.max_score
                except:
                    unattended.append(test_check.test_title)
            else:
                try:
                    test_score_item=Testscore.objects.get(test=test_check,student=student)
                    completed[test_check.test_title]=test_score_item.test_score
                    maximum_score[test_check.test_title]=test_check.max_score
                except:
                    ongoing.append(test_check.test_title)
        completed_list=zip(completed.iterkeys(),completed.itervalues(),maximum_score.itervalues())
        return render(request,'current_user.html',{'user':user,'upcoming':upcoming,'completed_list':completed_list,'ongoing':ongoing,'unattended':unattended})
    else:
        return redirect('/login/')

def logout_view(request):
    if request.user.is_authenticated():
        logout(request)
        return redirect('/login/')
    else:
        return redirect('/login/')
