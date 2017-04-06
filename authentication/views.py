from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
# Create your views here.
def signup( request ):
    error =[]
    form = StudentForm()
    form_department= StudentDepartmentForm()
    if request.method == "POST":
        post_values = request.POST
        if post_values['password'] == post_values["password_confirm"]:
            user_object = User.objects.create_user(username = post_values['username'],email = post_values['email'], password = post_values['username'],first_name = post_values['first_name'],last_name = post_values['last_name'])
            user_object.save();
            dept=Department.objects.filter(dept_code=post_values['department'])
            for i in dept:
                if i:
                    Student.objects.create(user =user_object,department=dept)
            return HttpResponse("Signup Successful")
        else:
            error.append("password doesnt match")
            return render(request,'sign_up.html',{'form':form,'form_department':form_department,'error':error})

    else:

        return render(request,'sign_up.html',{'form':form,'form_department':form_department,'error':error})

def log_in(request):
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
                return redirect('/tests/')
            else:
                error.append("User account is disabled")
        else:
            error.append("Invalid username or password")
        return render(request,'login.html',{'form':form,'error':error})
    else:
        return render(request,'login.html',{'form':form,'error':error})