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




def test_display(request,test_url,question_number):
    #test_athentication is a user defined helper in mcqfoss/helper.py
    if request.user.is_authenticated():
        if not test_authentication(request.user,test_url):
            return HttpResponse("You don't have permission to access this test")
        if request.method == 'POST':
            test = Test.objects.get(test_title = test_url )
            user = request.user
            student = Student.objects.get(user = user)
            question_item = Test.questions.get(question_no = question_no)
            if question_item.answer == request.post['options']:
                #switch to the much more efficient update_or_create
                try:
                    test_score_item = Testscore.objects.get(student =student,test = test)
                    test_score_item.test_score = test_score_item.test_score+1
                    test_score_item.save()
                except Testscore.DoesNotExist:
                    test_score_create = Testscore.objects.create(user = user,test =  test,test_score = 1,attempted = True)
            question_number_next = question_number+1
            next_question = "/tests/" + str(test_url)+"/" + str(question_number_next) + "/"
            return shortcut(next_question)
        else:
            first_filter = Test.objects.filter(test_title = test_url)
            test_item = first_filter[0].questions.filter(question_no = question_number) #Convert from filter to get
            invalid_message = check_valid( first_filter[0].start_time,first_filter[0].end_time,first_filter[0].date_of_exam )
            if invalid_message is None:
                return render(request,'question_page.html',{'test_item':test_item})
            else:
                return HttpResponse( invalid_message ) #Replace HttpResponse with a function to use it
    else:
        return redirect('/login/')
