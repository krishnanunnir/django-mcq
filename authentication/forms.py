from django import forms
from .models import *
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class StudentDepartmentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('department',)
