from django.http import HttpResponse
import time
def hello(request):
    return HttpResponse("Hello");
def current_time(request, offset):
    x = "The offset is %s and time is %s" %(int(offset),time.time());

    return HttpResponse(x);
