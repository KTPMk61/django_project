from django.db import models

CLS = (('Việt Nhật A', 'Việt Nhật A'), ('Việt Nhật B', 'Việt Nhật B'), ('Việt Nhật C', 'Việt Nhật C'),
       ('Việt Nhật D', 'Việt Nhật D'))
SUB = (('Kĩ Thuật Phần Mềm', 'Kĩ Thuật Phần Mềm'), ('Xác Suất Thống Kê', 'Xác Suất Thống Kê'), ('Math 4', 'Math 4'),
       ('Toán Rời Rạc', 'Toán Rời Rạc'))
class Student(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    fullname = models.CharField(max_length= 100)
    cls = models.CharField(max_length=30, choices=CLS)
    score = models.FloatField()
    score1 = models.FloatField()
    score2 = models.FloatField()
    score3 = models.FloatField()
    score4 = models.FloatField()
    sid = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    khoa = models.CharField(max_length=30)
    bir = models.DateTimeField()
    idSub = models.IntegerField(default=0)
    idCls = models.IntegerField(default=0)
    def __str__(self):
        return self.fullname
    def __str__(self):
        return self.username
    def __str__(self):
        return self.sid

class Teacher(models.Model):

    username = models.CharField(max_length=30,default='admin')
    password = models.CharField(max_length=20)
    fullname = models.CharField(max_length=30)
    cls = models.CharField(max_length=30,choices=CLS)
    email = models.CharField(max_length=20)
    khoa = models.CharField(max_length=30)
    subject = models.CharField(max_length= 30,choices=SUB)
    idSub = models.IntegerField(default=0)
    idCls = models.IntegerField(default=0)
class Student1(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    fullname = models.CharField(max_length= 100)
    cls = models.CharField(max_length=30, choices=CLS)
    score = models.FloatField()
    score1 = models.FloatField()
    score2 = models.FloatField()
    score3 = models.FloatField()
    score4 = models.FloatField()
    sid = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    khoa = models.CharField(max_length=30)
    bir = models.DateTimeField()
    idSub = models.IntegerField(default=0)
    idCls = models.IntegerField(default=0)
    def __str__(self):
        return self.fullname
    def __str__(self):
        return self.username
    def __str__(self):
        return self.sid
class Student2(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    fullname = models.CharField(max_length= 100)
    cls = models.CharField(max_length=30,choices=CLS)
    score = models.FloatField()
    score1 = models.FloatField()
    score2 = models.FloatField()
    score3 = models.FloatField()
    score4 = models.FloatField()
    sid = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    khoa = models.CharField(max_length=30)
    bir = models.DateTimeField()
    idSub = models.IntegerField(default=0)
    idCls = models.IntegerField(default=0)
    def __str__(self):
        return self.fullname
    def __str__(self):
        return self.username
    def __str__(self):
        return self.sid
class Student3(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    fullname = models.CharField(max_length= 100)
    cls = models.CharField(max_length= 30,choices=CLS)
    score = models.FloatField()
    score1 = models.FloatField()
    score2 = models.FloatField()
    score3 = models.FloatField()
    score4 = models.FloatField()
    sid = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    khoa = models.CharField(max_length=30)
    bir = models.DateTimeField()
    idSub = models.IntegerField(default=0)
    idCls = models.IntegerField(default=0)
    def __str__(self):
        return self.fullname
    def __str__(self):
        return self.username
    def __str__(self):
        return self.sid
class Classlist(models.Model):
    classname=models.CharField(max_length=30)
class Subjectlist(models.Model):
    subject = models.CharField(max_length= 30)
# Create your models here.
