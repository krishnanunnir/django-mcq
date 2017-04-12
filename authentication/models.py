from django.db import models
from django.contrib.auth.models import User
from exam.models import *

# Create your models here.
class Department(models.Model):
    dept_code = models.CharField( max_length = 100,blank=True, null=True )
    def __str__(self):
        return "%s" % self.dept_code


class Student(models.Model):
    user = models.OneToOneField( User,on_delete = models.CASCADE,related_name ='student' )
    department = models.ForeignKey(Department);
    def __str__(self):
        return "%s" % self.user.username

class Testscore(models.Model):
    student = models.ForeignKey(Student)
    test = models.ForeignKey( 'exam.Test' )
    test_score = models.IntegerField()
    attempted  = models.BooleanField(default = True)
