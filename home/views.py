from django.shortcuts import render
from .models import *
from .form import *
def home(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            password = form.cleaned_data['password']
            data = acount.objects.all()
            data1= lecturer.objects.all()
            data2= student.objects.all()
            for s in data:
                if s.username == user and s.password == password:
                    for s1 in data1:
                        if user==s1.phone_mail :
                            temp= lecturer.objects.get(id=s1.id)
                            acc= acount.objects.get(username=user)
                            return render(request, 'pages/teacher.html', {'teacher':temp,'acc':acc})
                    for s2 in data2:
                        if user==s2.mssv:
                            temp1= student.objects.get(id=s2.id)
                            acc1 = acount.objects.get(username=user)
                            return render(request, 'pages/student.html', {'student': temp1,'acc':acc1})
            return render(request, 'pages/fail1.html')
    return render(request, 'pages/login.html', {'form': form})
def register(request):
    form = TeacherRegisterForm()
    if request.method == 'POST':
        form = TeacherRegisterForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['email']
            data = acount.objects.all()
            for s in data:
                if s.username== user:
                    return render(request,'pages/fail.html')
            form.save()
            return render(request, 'pages/sucess.html')
    return render(request, 'pages/teacherreg.html', {'form': form})
def studentinf(request,idA,idS):
    a = acount.objects.get(id=idA)
    s= student.objects.get(id=idS)
    return render(request,'pages/studentinf.html',{'acc':a,'student':s})
def student_home(request,idA,idS):
    a = acount.objects.get(id=idA)
    s= student.objects.get(id=idS)
    return render(request,'pages/student.html',{'acc':a,'student':s})
def teacherview(request,idA,idS):
    a = acount.objects.get(id=idA)
    s = student.objects.get(id=idS)
    cls = student_class.objects.all()
    lectcls = lecturer_class.objects.all()
    teach = lecturer.objects.all()
    return render(request, 'pages/teacherinf.html', {'acc': a, 'student': s,'stclass':cls,'lectclass':lectcls,'teacher':teach})
