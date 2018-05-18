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
def viewclass(request,idA,idS):
    a = acount.objects.get(id=idA)
    s = student.objects.get(id=idS)
    cls = student_class.objects.all()
    clsname = grade.objects.all()
    return render(request, 'pages/viewclass.html', {'acc': a, 'student': s,'stcls':cls,'clsname':clsname})
def memcls(request,idA,idS,idC):
    a = acount.objects.get(id=idA)
    s = student.objects.get(id=idS)
    c = grade.objects.get(idcls=idC)
    data= student.objects.all()
    cls = student_class.objects.all()
    return render(request, 'pages/viewmem.html', {'acc': a, 'student': s,'class':c ,'stcls': cls,'data':data})
def teacher(request,idA,idT):
    a = acount.objects.get(id=idA)
    t = lecturer.objects.get(id=idT)
    return render(request, 'pages/teacher.html', {'acc': a, 'teacher': t})
def viewinfteacher(request,idA,idT):
    a = acount.objects.get(id=idA)
    t = lecturer.objects.get(id=idT)
    return render(request,'pages/viewinf.html',{'acc':a,'teacher':t})
def creatclass(request,idA,idT):
    idclass = 0
    check = 0
    idclass1 = 1
    a = acount.objects.get(id=idA)
    t = lecturer.objects.get(id=idT)
    st = student.objects.all()
    form = CreatClass()
    clas = grade.objects.all()
    data = subject.objects.all()
    if request.method =='POST':
        form = CreatClass(request.POST)
        if form.is_valid():
            subname = form.cleaned_data['subname']
            subcode = form.cleaned_data['subcode']
            clsname = form.cleaned_data['classname']
            for s in clas:
                check=check+1
                if s.name != clsname:
                    idclass=idclass+1
            if check==idclass and check!=0:
                for s1 in clas:
                    idclass1 = idclass1 + 1
                for s2 in data:
                    if s2.subject_code == subcode:
                        subjectId = s2.subjectId
                sub = grade(idcls=idclass1, name=clsname, subjectId=subjectId)
                sub.save()
                #return render(request, 'pages/addmem.html', {'acc': a, 'teacher': t,'student':st})
            if check==0:
                for s2 in data:
                    if s2.subject_code == subcode:
                        subjectId= s2.subjectId
                sub = grade(idcls=idclass1, name=clsname, subjectId=subjectId)
                sub.save()
                #return render(request,'pages/addmem.html',{'acc': a, 'teacher': t,'student':st})
            if idclass<check :
                return render(request,'pages/failcreate.html',{'acc': a, 'teacher': t,'form':form})
    return render(request, 'pages/creatclass.html', {'acc': a, 'teacher': t,'form':form})