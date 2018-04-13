from django.db import models
class Student(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    fullname = models.CharField(max_length= 100)
    score = models.IntegerField()
    sid = models.CharField(max_length=20)
    def __str__(self):
        return self.fullname
    def __str__(self):
        return self.username
    def __str__(self):
        return self.sid
# Create your models here.
