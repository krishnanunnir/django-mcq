from django.shortcuts import render
from .forms import *
# Create your views here.
def signup( request ):
    form = StudentForm()
    form_department= StudentDepartmentForm()
    return render(request,'sign_up.html',{'form':form,'form_department':form_department})
