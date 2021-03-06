from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.forms.models import modelformset_factory
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
def update(request,idCls,id):
    teacher = Teacher.objects.get(id=id)
    if idCls==1:
        if teacher.idSub ==1:
            data = Student.objects.all()
            Update = modelformset_factory(Student, fields=["score", ], labels={'score': 'DiemKTPM'}, extra=0)
            formset = Update(request.POST or None)
            if formset.is_valid():
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.user = request.user
                    instance.save()
        if teacher.idSub ==2:
            data = Student.objects.all()
            Update = modelformset_factory(Student, fields=["score1", ], labels={'score1': 'Điểm Math4'}, extra=0)
            formset = Update(request.POST or None)
            if formset.is_valid():
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.user = request.user
                    instance.save()
        if teacher.idSub ==3:
            data = Student.objects.all()
            Update = modelformset_factory(Student, fields=["score2", ], labels={'score2': 'Điểm SXTK'}, extra=0)
            formset = Update(request.POST or None)
            if formset.is_valid():
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.user = request.user
                    instance.save()
        if teacher.idSub ==4:
            data = Student.objects.all()
            Update = modelformset_factory(Student, fields=["score3", ], labels={'score3': 'Toan Roi Rac'}, extra=0)
            formset = Update(request.POST or None)
            if formset.is_valid():
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.user = request.user
                    instance.save()
    if idCls==2:
        if teacher.idSub ==1:
            data = Student1.objects.all()
            Update = modelformset_factory(Student1, fields=["score", ], labels={'score': 'DiemKTPM'}, extra=0)
            formset = Update(request.POST or None)
            if formset.is_valid():
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.user = request.user
                    instance.save()
        if teacher.idSub ==2:
            data = Student1.objects.all()
            Update = modelformset_factory(Student1, fields=["score1", ], labels={'score1': 'Điểm Math4'}, extra=0)
            formset = Update(request.POST or None)
            if formset.is_valid():
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.user = request.user
                    instance.save()
        if teacher.idSub ==3:
            data = Student1.objects.all()
            Update = modelformset_factory(Student1, fields=["score2", ], labels={'score2': 'Điểm SXTK'}, extra=0)
            formset = Update(request.POST or None)
            if formset.is_valid():
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.user = request.user
                    instance.save()
        if teacher.idSub ==4:
            data = Student1.objects.all()
            Update = modelformset_factory(Student1, fields=["score3", ], labels={'score3': 'Toan Roi Rac'}, extra=0)
            formset = Update(request.POST or None)
            if formset.is_valid():
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.user = request.user
                    instance.save()
    if idCls==3:
        if teacher.idSub ==1:
            data = Student2.objects.all()
            Update = modelformset_factory(Student2, fields=["score", ], labels={'score': 'DiemKTPM'}, extra=0)
            formset = Update(request.POST or None)
            if formset.is_valid():
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.user = request.user
                    instance.save()
        if teacher.idSub ==2:
            data = Student2.objects.all()
            Update = modelformset_factory(Student2, fields=["score1", ], labels={'score1': 'Điểm Math4'}, extra=0)
            formset = Update(request.POST or None)
            if formset.is_valid():
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.user = request.user
                    instance.save()
        if teacher.idSub ==3:
            data = Student2.objects.all()
            Update = modelformset_factory(Student2, fields=["score2", ], labels={'score2': 'Điểm SXTK'}, extra=0)
            formset = Update(request.POST or None)
            if formset.is_valid():
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.user = request.user
                    instance.save()
        if teacher.idSub ==4:
            data = Student2.objects.all()
            Update = modelformset_factory(Student2, fields=["score3", ], labels={'score3': 'Toan Roi Rac'}, extra=0)
            formset = Update(request.POST or None)
            if formset.is_valid():
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.user = request.user
                    instance.save()
    if idCls==4:
        if teacher.idSub ==1:
            data = Student3.objects.all()
            Update = modelformset_factory(Student3, fields=["score", ], labels={'score': 'DiemKTPM'}, extra=0)
            formset = Update(request.POST or None)
            if formset.is_valid():
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.user = request.user
                    instance.save()
        if teacher.idSub ==2:
            data = Student3.objects.all()
            Update = modelformset_factory(Student3, fields=["score1", ], labels={'score1': 'Điểm Math4'}, extra=0)
            formset = Update(request.POST or None)
            if formset.is_valid():
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.user = request.user
                    instance.save()
        if teacher.idSub ==3:
            data = Student3.objects.all()
            Update = modelformset_factory(Student3, fields=["score2", ], labels={'score2': 'Điểm SXTK'}, extra=0)
            formset = Update(request.POST or None)
            if formset.is_valid():
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.user = request.user
                    instance.save()
        if teacher.idSub ==4:
            data = Student3.objects.all()
            Update = modelformset_factory(Student3, fields=["score3", ], labels={'score3': 'Toan Roi Rac'}, extra=0)
            formset = Update(request.POST or None)
            if formset.is_valid():
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.user = request.user
                    instance.save()
    return render(request,'pages/KTPM.html',{'teacher':teacher,'data':data,'formset':formset})
def teacher(request,idCls,id):
    teacher= Teacher.objects.get(id=id)
    return render(request, 'pages/teacher.html', {'teacher': teacher,})
def viewinf(request,idCls,id):
    teacher = Teacher.objects.get(id=id)
    return render(request,'pages/viewinf.html',{'teacher':teacher})
def search(request,idCls,id):
    teacher = Teacher.objects.get(id=id)
    student = Student.objects.all()
    student1 = Student1.objects.all()
    student2 = Student2.objects.all()
    student3 = Student3.objects.all()
    form = Search()
    if request.method == 'POST':
        form = Search(request.POST)
        if form.is_valid():
            for s in student:
                if s.fullname == form.cleaned_data['fullname'] and s.sid == form.cleaned_data['sid']:
                    score = Student.objects.get(id=s.id)
                    return render(request, 'pages/result.html', {'score': score, 'teacher': teacher})
            for s in student1:
                if s.fullname == form.cleaned_data['fullname'] and s.sid == form.cleaned_data['sid']:
                    score = Student.objects.get(id=s.id)
                    return render(request, 'pages/result.html', {'score': score, 'teacher': teacher})
            for s in student2:
                if s.fullname == form.cleaned_data['fullname'] and s.sid == form.cleaned_data['sid']:
                    score = Student.objects.get(id=s.id)
                    return render(request, 'pages/result.html', {'score': score, 'teacher': teacher})
            for s in student3:
                if s.fullname == form.cleaned_data['fullname'] and s.sid == form.cleaned_data['sid']:
                    score = Student.objects.get(id=s.id)
                    return render(request, 'pages/result.html', {'score': score, 'teacher': teacher})
    return render(request, 'pages/searchst.html', {'teacher': teacher, 'form': form})

def viewclasst(request,idCls,id):
    teacher= Teacher.objects.get(id=id)
    if idCls == 1:
        data = Student.objects.all()
    if idCls == 2:
        data = Student1.objects.all()
    if idCls == 3:
        data = Student2.objects.all()
    if idCls == 4:
        data = Student3.objects.all()
    return render(request,'pages/viewclasst.html',{'teacher':teacher,'data':data})