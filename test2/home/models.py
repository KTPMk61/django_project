from django.db import models
class Student(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    fullname = models.CharField(max_length= 100)
    score = models.IntegerField()
    score1 = models.IntegerField()
    score2 = models.IntegerField()
    score3 = models.IntegerField()
    sid = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    khoa = models.CharField(max_length=30)
    bir = models.DateTimeField()
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
    email = models.CharField(max_length=20)
    khoa = models.CharField(max_length=30)
    bir = models.DateTimeField()
    subject = models.CharField(max_length= 30)

# Create your models here.
