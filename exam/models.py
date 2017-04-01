from django.db import models

# Create your models here.

class Option(models.Model):
    option_value = models.TextField()

class Question(models.Model):
    question_no = models.IntegerField()
    question_text = models.TextField()
    answer = models.CharField( max_length = 100 );
    options = models.ManyToManyField(Option)



class Test(models.Model):
    teacher = models.CharField( max_length = 30 )
    date_of_exam = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    questions = models.ManyToManyField(Question)
