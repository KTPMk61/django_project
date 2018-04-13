from django import forms
import re
from .models import Student
class RegistrationForm(forms.Form):
    fullname = forms.CharField(label = 'Họ Tên', max_length= 30)
    sid = forms.CharField(label='MSSV', max_length=30)
    username = forms.CharField(label = 'Tài khoản', max_length= 30)
    password =  forms.CharField(label= 'Mật khẩu',widget= forms.PasswordInput())
    def save(self):
        fullname = self.cleaned_data['fullname']
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        sid = self.cleaned_data['sid']
        s = Student(username = username, password = password, fullname= fullname,score= 0,sid= sid)
        s.save()
class LoginForm(forms.Form):
    username = forms.CharField(label = 'Tài khoản', max_length= 30)
    password =  forms.CharField(label= 'Mật khẩu',widget= forms.PasswordInput())
