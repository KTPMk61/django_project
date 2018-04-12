from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'pages/home.html')
def student(request):
    return render(request,'pages/student.html')
def teacher(request):
    return render(request,'pages/teacher.html')
# Create your views here.
