from django.shortcuts import render,redirect
from .forms import *
from .models import *
def home(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            password = form.cleaned_data['password']
            data = Student.objects.all()
            for s in data:
                if s.username == user and s.password == password:
                    score = Student.objects.get(id=s.id)
                    return render(request, 'pages/student.html', {'score': score})
            data1 = Student1.objects.all()
            for s in data1:
                if s.username == user and s.password == password:
                    score = Student.objects.get(id=s.id)
                    return render(request, 'pages/student.html', {'score': score})
            data2 = Student2.objects.all()
            for s in data2:
                if s.username == user and s.password == password:
                    score = Student.objects.get(id=s.id)
                    return render(request, 'pages/student.html', {'score': score})
            data3 = Student3.objects.all()
            for s in data3:
                if s.username == user and s.password == password:
                    score = Student.objects.get(id=s.id)
                    return render(request, 'pages/student.html', {'score': score})
            tc = Teacher.objects.all()
            for s in tc:
                if s.username == user and s.password == password:
                    teacher = Teacher.objects.get(id=s.id)
                    return render(request, 'pages/teacher.html', {'teacher': teacher})
            return render(request, 'pages/fail1.html')
    return render(request,'pages/login.html',{'form': form})
def reg(request):
    return render(request,'pages/register.html')
def regs(request):
    form = StudentRegisterForm()
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            user = form.cleaned_data['username']
            password = form.cleaned_data['password']
            data = Student.objects.all()
            for s in data:
                if s.username == user:
                    return render(request, 'pages/fail.html')
            data1 = Student1.objects.all()
            for s in data1:
                if s.username == user:
                    return render(request, 'pages/fail.html')
            data2 = Student2.objects.all()
            for s in data2:
                if s.username == user:
                    return render(request, 'pages/fail.html')
            data3 = Student3.objects.all()
            for s in data3:
                if s.username == user:
                    return render(request, 'pages/fail.html')
            form.save()
            return render(request, 'pages/sucess.html')
    return render(request,'pages/studentreg.html',{'form':form})
def regt(request):
    form = TeacherRegisterForm()
    if request.method== 'POST':
        form= TeacherRegisterForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            subject = form.cleaned_data['subject']
            cls = form.cleaned_data['cls']
            data = Teacher.objects.all()
            for s in data:
                if s.username==user:
                    return render(request, 'pages/fail.html')
                elif s.subject==subject and s.cls==cls:
                    return render(request,'pages/fail2.html')
            form.save()
            return render(request, 'pages/sucess.html')
    return render(request,'pages/teacherreg.html',{'form':form})
def teacherinf(request,idCls,id):
    teacher= Teacher.objects.all()
    if idCls==1:
        score = Student.objects.get(id=id)
    if idCls == 2:
        score = Student1.objects.get(id=id)
    if idCls == 3:
        score = Student2.objects.get(id=id)
    if idCls == 4:
        score = Student3.objects.get(id=id)
    return render(request,'pages/teacherinf.html',{'teacher':teacher,'score':score})
def student(request,idCls,id):
    teacher = Teacher.objects.all()
    if idCls == 1:
        score = Student.objects.get(id=id)
    if idCls == 2:
        score = Student1.objects.get(id=id)
    if idCls == 3:
        score = Student2.objects.get(id=id)
    if idCls == 4:
        score = Student3.objects.get(id=id)
    return render(request, 'pages/student.html', {'teacher': teacher, 'score': score})
def studentinf(request,idCls,id):
    if idCls == 1:
        score = Student.objects.get(id=id)
    if idCls == 2:
        score = Student1.objects.get(id=id)
    if idCls == 3:
        score = Student2.objects.get(id=id)
    if idCls == 4:
        score = Student3.objects.get(id=id)
    return render(request, 'pages/studentinf.html', {'score': score})
def viewclass(request,idCls,id):
    if idCls == 1:
        data = Student.objects.all()
        score = Student.objects.get(id=id)
    if idCls == 2:
        data = Student1.objects.all()
        score = Student1.objects.get(id=id)
    if idCls == 3:
        data = Student2.objects.all()
        score = Student2.objects.get(id=id)
    if idCls == 4:
        data = Student3.objects.all()
        score = Student3.objects.get(id=id)
    return render(request, 'pages/viewclass.html', {'score': score,'data':data})