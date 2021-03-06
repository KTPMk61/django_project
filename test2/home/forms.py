from django import forms
from .models import *

CLS = (('Việt Nhật A', 'Việt Nhật A'), ('Việt Nhật B', 'Việt Nhật B'), ('Việt Nhật C', 'Việt Nhật C'),
       ('Việt Nhật D', 'Việt Nhật D'))
SUB = (('Kĩ Thuật Phần Mềm', 'Kĩ Thuật Phần Mềm'), ('Xác Suất Thống Kê', 'Xác Suất Thống Kê'), ('Math 4', 'Math 4'),
       ('Toán Rời Rạc', 'Toán Rời Rạc'))
class LoginForm(forms.Form):
    username = forms.CharField(label = 'Tài khoản', max_length= 30)
    password =  forms.CharField(label= 'Mật khẩu',widget= forms.PasswordInput())
class StudentRegisterForm(forms.Form):
    fullname = forms.CharField(label = 'Họ Tên', max_length= 30)
    sid = forms.CharField(label='MSSV', max_length=30)
    khoa = forms.CharField(label='Khoa/Vien',max_length=30)
    email = forms.CharField(label='Emails/SDT',max_length=30)
    cls = forms.ChoiceField(label="Lớp :", choices=CLS, initial='', widget=forms.Select(), required=False)
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
        cls = self.cleaned_data['cls']
        data = Classlist.objects.all()
        index=0
        for s in data:
            if s.classname == cls:
                index = s.id
        if index==1:
            a = Student(username = username, password = password, fullname= fullname,score= 0,score1=0,score2=0,score3=0,score4=0,sid= sid,khoa= khoa,bir=bir,email= email,idCls=1,idSub=0,cls=cls)
            a.save()
        if index==2:
            a = Student1(username = username, password = password, fullname= fullname,score= 0,score1=0,score2=0,score3=0,score4=0,sid= sid,khoa= khoa,bir=bir,email= email,idCls=2,idSub=0,cls=cls)
            a.save()
        if index==3:
            a = Student2(username = username, password = password, fullname= fullname,score= 0,score1=0,score2=0,score3=0,score4=0,sid= sid,khoa= khoa,bir=bir,email= email,idCls=3,idSub=0,cls=cls)
            a.save()
        if index==4:
            a = Student3(username = username, password = password, fullname= fullname,score= 0,score1=0,score2=0,score3=0,score4=0,sid= sid,khoa= khoa,bir=bir,email= email,idCls=4,idSub=0,cls=cls)
            a.save()

class TeacherRegisterForm(forms.Form):

    fullname = forms.CharField(label = 'Họ Tên', max_length= 30)
    subject = forms.ChoiceField(label="Môn Giảng Dạy",choices=SUB, initial='',widget=forms.Select(),required= False)
    khoa = forms.CharField(label='Khoa/Vien',max_length=30)
    email = forms.CharField(label='Emails/SDT',max_length=30)
    cls = forms.ChoiceField(label="Lớp Giảng Dạy",choices=CLS, initial='',widget=forms.Select(),required= False)
    username = forms.CharField(label = 'Tài khoản', max_length= 30)
    password =  forms.CharField(label= 'Mật khẩu',widget= forms.PasswordInput())
    def save(self):
        fullname = self.cleaned_data['fullname']
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        subject = self.cleaned_data['subject']
        khoa = self.cleaned_data['khoa']
        email = self.cleaned_data['email']
        cls = self.cleaned_data['cls']
        data = Classlist.objects.all()
        data1 = Subjectlist.objects.all()
        index=0
        index1=0
        for s in data:
            if s.classname==cls:
                index=s.id
        for s1 in data1:
            if s1.subject == subject:
                index1 = s1.id
        a = Teacher(username = username, password = password, email = email,fullname= fullname,khoa= khoa,subject=subject,cls=cls,idCls=index,idSub=index1)
        a.save()
class Search(forms.Form):
    fullname= forms.CharField(label = 'Tên Sinh Viên',max_length=30)
    sid = forms.CharField(label='MSSV',max_length=30)
