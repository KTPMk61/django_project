from django import forms
import re
from .models import Student
class RegistrationForm(forms.Form):
    fullname = forms.CharField(label = 'Họ Tên', max_length= 30)
    sid = forms.CharField(label='MSSV', max_length=30)
    khoa = forms.CharField(label='Khoa/Vien',max_length=30)
    email = forms.CharField(label='Emails/SDT',max_length=30)
    bir = forms.DateTimeField(label='Ngay Sinh',input_formats=['%d/%m/%Y'])
    username = forms.CharField(label = 'Tài khoản', max_length= 30)
    password =  forms.CharField(label= 'Mật khẩu',widget= forms.PasswordInput())
    def save(self):
        fullname = self.cleaned_data['fullname']
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        sid = self.cleaned_data['sid']
        khoa = self.cleaned_data['khoa']
        email = self.cleaned_data['email']
        bir = self.cleaned_data['bir']
        s = Student(username = username, password = password, fullname= fullname,score= 0,sid= sid,khoa= khoa,bir=bir,email= email)
        s.save()
class LoginForm(forms.Form):
    username = forms.CharField(label = 'Tài khoản', max_length= 30)
    password =  forms.CharField(label= 'Mật khẩu',widget= forms.PasswordInput())
class UpdateScore(forms.ModelForm):
    score = forms.IntegerField(label='Điểm mới')
class UpdateScore1(forms.ModelForm):
    score = forms.IntegerField(label= 'SXTK')

