from django.db import models
class Student(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    fullname = models.CharField(max_length= 100)
    def __str__(self):
        return self.name
# Create your models here.
