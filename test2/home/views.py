from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .forms import RegistrationForm,LoginForm,UpdateScore,UpdateScore1
from django.forms.models import modelformset_factory
from .models import Student,Teacher
def index(request):
    return render(request,'pages/home.html')
def student(request,id):
    score = Student.objects.get(id=id)
    return render(request, 'pages/student.html', {'score': score})
def teacher(request,id):
    teacher = Teacher.objects.get(id=id)
    return render(request,'pages/teacher.html',{'teacher':teacher})
def reg(request):
    form= RegistrationForm()
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            user = form.cleaned_data['username']
            password = form.cleaned_data['password']
            data = Student.objects.all()
            for s in data:
                if s.username == user:
                    return render(request,'pages/fail.html')
            form.save()
            return render(request,'pages/sucess.html')
    return render(request,'pages/register.html',{'form':form})
def login(request):
    form= LoginForm()
    if request.method == 'POST':
        form= LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            password = form.cleaned_data['password']
            data = Student.objects.all()
            for s in data:
                if s.username == user and s.password == password:
                    score = Student.objects.get(id=s.id)
                    return render(request,'pages/student.html',{'score':score})
            tc = Teacher.objects.all()
            for s in tc:
                if s.username == user and s.password == password:
                    teacher = Teacher.objects.get(id = s.id)
                    return render(request,'pages/teacher.html',{'teacher':teacher})
            return render(request,'pages/fail1.html')
    return render(request,'pages/login.html',{'form': form})
def viewscore(request,id):
    score = Student.objects.get(id =id)
    args ={'score':score}
    return render(request,'pages/viewscore.html',args)
def viewclass(request,id):
    score = Student.objects.get(id=id)
    data = {'data':Student.objects.all(),'score':score}
    return render(request,'pages/viewclass.html',data)
def viewinf(request,id):
    teacher = Teacher.objects.get(id = id)
    return render(request,'pages/viewinf.html',{'teacher':teacher})
def viewclasst(request,id):
    teacher= Teacher.objects.get(id = id)
    data = {'data':Student.objects.all(),'teacher':teacher}
    return render(request,'pages/viewclasst.html',data)
def update(request,id):
    teacher = Teacher.objects.get(id=id)
    if id == 1 :
        return redirect('/KTPM/1')
    elif id ==2:
        return redirect('/SXTK/2')
def KTPM(request,id):
    teacher = Teacher.objects.get(id=id)
    Update = modelformset_factory(Student, fields=["score",],labels={'score': 'DiemKTPM'}, extra=0)
    formset = Update(request.POST or None)
    if formset.is_valid():
        instances = formset.save(commit=False)
        for instance in instances:
            instance.user = request.user
            instance.save()
    return render(request, 'pages/update.html', {'teacher': teacher, 'formset': formset, 'data': Student.objects.all()})
def SXTK(request,id):
    teacher = Teacher.objects.get(id=id)
    field_list=['score1',]
    Update = modelformset_factory(Student, fields=field_list,labels={'score1':'Diem SXTK'}, extra=0)
    formset = Update(request.POST or None)
    if formset.is_valid():
        instances = formset.save(commit=False)
        for instance in instances:
            instance.user = request.user
            instance.save()
    return render(request, 'pages/update.html', {'teacher': teacher, 'formset': formset, 'data': Student.objects.all()})
def teacherinf(request,id):
    score = Student.objects.get(id=id)

    return render(request,'pages/teacherinf.html',{'score':score,'teacher': Teacher.objects.all()})