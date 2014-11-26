from django.db import models
from django.contrib.auth.models import User
from students.models import Student

class Teacher(User):
    e_mail = models.CharField(max_length=30)

class Class(models.Model):
    name = models.Charfield(max_length=30)
    teacher = models.ManyToManyField(Teacher)
    student = models.ManyToManyField(Student)