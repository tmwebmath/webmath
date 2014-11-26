from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Bryan ( pas sûr )

class Teacher(User):
    e_mail = models.CharField(max_length=30)
    
class Student(User):
    pass

class Class(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ManyToManyField(Teacher)
    student = models.ManyToManyField(Student)