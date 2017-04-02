from django.contrib import admin
from .models import *


# Register your models here.
class testAdmin(admin.ModelAdmin):
    list_display=('test_title','date_of_exam','start_time','end_time')
admin.site.register(Question)
admin.site.register(Test,testAdmin)
