from django.shortcuts import render
from .models import *
from django.http import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout
from authentication.models import *
from mcqfoss.helper import *

# Create your views here.
def home(request):
    if  not request.user.is_authenticated():
        return redirect('/login/')
    else:
        return redirect('/current_user/')

def test_display(request,test_url):
    #test_athentication is a user defined helper in mcqfoss/helper.py
    if request.user.is_authenticated():
        if not test_authentication(request.user,test_url):
            return HttpResponse("You don't have permission to access this test")
        test = Test.objects.get(test_title = test_url )
        maximum_score=test.max_score
        user = request.user
        student = Student.objects.get(user = user)
        try:
            test_score_item=Testscore.objects.filter(test=test,student=student)
            if bool(test_score_item):
                return HttpResponse("Sorry, test has already been attended")
        except:
            pass
        if request.method == 'POST':
            answer_values={}
            question_dictionary={}
            remark={}
            score={}
            test_score=0
            answer_values=cleaned_post(request.POST)
            for question,answer in answer_values.items():
                selected_question = Test.objects.get(test_title = test_url).questions.get(question_no=question)
                question_dictionary[question]=selected_question.question_text
                if(answer==selected_question.answer):
                    remark[question]="Correct"
                    score[question]="+1"
                    test_score+=1
                elif(answer!=selected_question.answer):
                    remark[question]="Wrong"
                    score[question]="+0"
                else:
                    remark[question]="Not attempted"
                    score[question]="+0"
            Testscore.objects.create(student=student,test=test,test_score=test_score)
            percentage = (  100.0*test_score)/maximum_score
            list_question = zip(answer_values.iterkeys(),answer_values.itervalues(),question_dictionary.itervalues(),remark.itervalues(),score.itervalues())
            return render(request,'post_check.html',{'list_question':list_question,'test_score':test_score,'max_score':maximum_score,'percentage':percentage,'user':user})
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

def display_scores(request,offset):
    test = Test.objects.get(test_title = offset )
    maximum_score = test.max_score
    test_score_item=Testscore.objects.filter(test=test)
    return render(request,'score_page.html',{'test_scores':test_score_item,'test_name':test.test_title,'maximum_score':maximum_score})
