from django.db import models

# Create your models here.



class Question(models.Model):
    question_no = models.IntegerField(blank=True, null=True)
    question_text = models.TextField(blank=True, null=True)
    answer = models.CharField( max_length = 100 ,blank=True, null=True)
    option_one = models.CharField(max_length=200,blank=True, null=True)
    option_two = models.CharField(max_length=200,blank=True, null=True)
    option_three = models.CharField(max_length=200,blank=True, null=True)
    option_four = models.CharField(max_length=200,blank=True, null=True)
    option_five = models.CharField(max_length=200,blank=True, null=True)
    def __str__(self):
        return "%s" % self.question_no


class Test(models.Model):
    test_title = models.CharField( max_length = 100, default="Generic Test" ,blank=True, null=True)
    teacher = models.CharField( max_length = 30 ,blank=True, null=True)
    date_of_exam = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    questions = models.ManyToManyField(Question,blank=True, null=True)
