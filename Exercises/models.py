from django.db import models

# Create your models here.

#Bryan ( pas sûr )

class Teacher(models.User):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    e_mail = models.CharField(max_length=30)
    
class Student(models.User):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
class Class(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    teacher = models.ManyToMany(Teacher)
    student = models.ManyToMany(Student)
