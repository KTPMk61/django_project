from django import forms
import re
from .models import Student
class RegistrationForm(forms.Form):
    fullname = forms.CharField(label = 'Ho Ten', max_length= 30)
    username = forms.CharField(label = 'Tai khoan', max_length= 30)
    password =  forms.CharField(label= 'Mat khau',widget= forms.PasswordInput())
    def save(self):
        fullname = self.cleaned_data['fullname']
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        s = Student(username = username, password = password, fullname= fullname)
        s.save()
class LoginForm(forms.Form):
    username = forms.CharField(label = 'Tai khoan', max_length= 30)
    password =  forms.CharField(label= 'Mat khau',widget= forms.PasswordInput())