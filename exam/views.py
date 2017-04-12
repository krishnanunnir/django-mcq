from django.shortcuts import render
from .models import *
from django.http import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout
from authentication.models import *
# Create your views here.


def tests(request):
    if  request.user.is_authenticated():
        user = Student.objects.filter( username = request.user.name )
        test_items = Test.objects.all(department = user.department );
        return render(request, 'tests.html', {'test_items': test_items})
    else:
            return redirect('/login/')




def test_display(request,test_url,question_number):
    if request.user.is_authenticated():
        if request.method == 'POST':
            return render(request,'post_check.html',{'post_items':request.POST.items()})
        else:
            first_filter = Test.objects.filter(test_title = test_url)
            test_item = first_filter[0].questions.filter(question_no = question_number)
            return render(request,'question_page.html',{'test_item':test_item})
    else:
        return redirect('/login/')
