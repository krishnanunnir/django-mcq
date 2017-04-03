from django.shortcuts import render
from .models import *
from django.http import *
# Create your views here.
def tests(request):
    test_items = Test.objects.all();
    return render(request, 'tests.html', {'test_items': test_items})

def test_display(request,test_url,question_number):
    if request.method == 'POST':
        x = request.POST.get('options2')
        return HttpResponse(x)
    else:
        first_filter = Test.objects.filter(test_title = test_url)
        test_item = first_filter[0].questions.filter(question_no = question_number)
        return render(request,'question_page.html',{'test_item':test_item})
