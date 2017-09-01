from django.db import models
from authentication.models import *
# Create your models here.



class Question(models.Model):
    question_no = models.IntegerField(default=1)
    question_text = models.TextField(default="")
    answer = models.CharField( max_length = 100,default="" )
    option_one = models.CharField(max_length=200,default="" )
    option_two = models.CharField(max_length=200,default="")
    option_three = models.CharField(max_length=200,default="")
    option_four = models.CharField(max_length=200,default="")
    option_five = models.CharField(max_length=200,blank=True, null=True)
    def __str__(self):
        return "%s.%s" % (self.question_no,self.question_text)


class Test(models.Model):
    test_title = models.CharField( max_length = 100, default="GenericTest" )
    teacher = models.CharField( max_length = 30,default="Vipin Sir")
    date_of_exam = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    max_score = models.IntegerField(default=0)
    permitted_for = models.ForeignKey( 'authentication.Department',default = 0)
    questions = models.ManyToManyField(Question)
    def __str__(self):
        return "%s" % (self.test_title)
