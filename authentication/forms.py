from django import forms
from .models import *
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'password_confirm', 'email')
    def clean(self):
        cleaned_data = super(Student, self).clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("confirm_password")
        return cleaned_data
"""        if password != password_confirm:
            Form validation not wokring here for some reason, so have setup a alternate cleaning funvtion in authentication views.
            raise forms.ValidationError("password and confirm_password does not match")"""

class StudentDepartmentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('department',)

class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
