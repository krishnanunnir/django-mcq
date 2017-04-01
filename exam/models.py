from django.db import models

# Create your models here.

class Option(models.Model):
    option_value = models.TextField(blank=True, null=True)

class Question(models.Model):
    question_no = models.IntegerField(blank=True, null=True)
    question_text = models.TextField(blank=True, null=True)
    answer = models.CharField( max_length = 100 ,blank=True, null=True);
    options = models.ManyToManyField(Option,blank=True, null=True)



class Test(models.Model):
    test_title = models.CharField( max_length = 100, default="Generic Test" ,blank=True, null=True)
    teacher = models.CharField( max_length = 30 ,blank=True, null=True)
    date_of_exam = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    questions = models.ManyToManyField(Question,blank=True, null=True)
