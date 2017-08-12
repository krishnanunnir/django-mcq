from django.shortcuts import render
from .models import *
from django.http import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout
from authentication.models import *
from mcqfoss.helper import *

# Create your views here.


def tests(request):
    if  request.user.is_authenticated():
        user = Student.objects.get( user__username = request.user.username )
        test_items = Test.objects.filter( permitted_for = user.department  )
        return render(request, 'tests.html', {'test_items': test_items})
    else:
            return redirect('/login/')




def test_display(request,test_url):
    #test_athentication is a user defined helper in mcqfoss/helper.py
    if request.user.is_authenticated():
        if not test_authentication(request.user,test_url):
            return HttpResponse("You don't have permission to access this test")
        if request.method == 'POST':
            answer_values={}
            result={}
            test = Test.objects.get(test_title = test_url )
            user = request.user
            student = Student.objects.get(user = user)
            answer_values=cleaned_post(request.POST)

            return render(request,'post_check.html',{'post_items':answer_values})
        else:
            first_filter = Test.objects.get(test_title = test_url)
            test_item = first_filter.questions.all()
            invalid_message = check_valid( first_filter.start_time,first_filter.end_time,first_filter.date_of_exam )
            if invalid_message is None:
                return render(request,'question_page.html',{'test_item':test_item,'test_url':test_url})
            else:
                return HttpResponse( invalid_message ) #Replace HttpResponse with a function to use it
    else:
        return redirect('/login/')
