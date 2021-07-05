from django.db import models

class Student(models.Model):
    sid = models.CharField(max_length=50)
    sname = models.CharField(max_length=100)
    semail = models.EmailField()
    scontact = models.CharField(max_length=50)
     
