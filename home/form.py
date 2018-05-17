from django import forms
from .models import *
class LoginForm(forms.Form):
    username = forms.CharField(label = 'Tài khoản', max_length= 30)
    password =  forms.CharField(label= 'Mật khẩu',widget= forms.PasswordInput())
class TeacherRegisterForm(forms.Form):
    fullname = forms.CharField(label = 'Họ Tên', max_length= 30)
    khoa = forms.CharField(label='Khoa/Vien',max_length=30)
    email = forms.CharField(label='Emails/SDT',max_length=30)
    bir = forms.CharField(label='Ngay sinh',max_length=30)
    password =  forms.CharField(label= 'Mật khẩu',widget= forms.PasswordInput())
    def save(self):
        fullname = self.cleaned_data['fullname']
        password = self.cleaned_data['password']
        khoa = self.cleaned_data['khoa']
        email = self.cleaned_data['email']
        bir = self.cleaned_data['bir']
        a =lecturer(name = fullname,phone_mail= email,institute= khoa,birthday= bir)
        b = acount(username = email,password= password)
        b.save()
        a.save()
