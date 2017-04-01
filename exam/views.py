from django.shortcuts import render
from .models import *
# Create your views here.
def tests(request):
    test_items = Test.objects.all();
    return render(request, 'tests.html', {'test_items': test_items})
