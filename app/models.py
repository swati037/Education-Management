from django.db import models

# Create your models here.
class log(models.Model):
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=50)

class log1(models.Model):
    username1 = models.CharField(max_length=122)
    email1 = models.CharField(max_length=122)
    password1 = models.CharField(max_length=50)

class subject(models.Model):
    email = models.CharField(max_length=100, default="")    
    name = models.ManyToManyField('log')
    subjectname = models.CharField(max_length=30)

class ass(models.Model):
    email = models.CharField(max_length=100, default="")    
    subjectname = models.CharField(max_length=30, default="")
    question = models.CharField(max_length=800, default="")
    time = models.CharField(max_length=30, default="")
    date = models.CharField(max_length=30, default="")

class testtable(models.Model):
    email3 = models.CharField(max_length=100, default="")    
    subjectname3 = models.CharField(max_length=30, default="")
    question3 = models.CharField(max_length=800, default="")
    time3 = models.CharField(max_length=30, default="")

