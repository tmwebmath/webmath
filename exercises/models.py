from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    skill = models.CharField(max_length=200)
    chapter = models.ManyToManyField('teachers.Chapter')
    
#
# all about exercise
#
class Exercise_type(models.Model):
    title = models.CharField(max_length=20)
    exercise = models.ForeignKey('Exercise')
    donnees = models.CharField(max_length=50)
    user = models.ManyToManyField('students.Student')
    skill = models.ManyToManyField(Skill)
    
    

class Exercise(models.Model):
    user = models.ManyToManyField('students.Student')
    author = models.ForeignKey('teachers.Teacher')
    chapter = models.ManyToManyField('teachers.Chapter')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    num_exercise = models.IntegerField()
    grade = models.CharField(max_length=60)
    type_donnees = models.ForeignKey(Exercise_type)
    indices = models.CharField(max_length=50)
    commentary = models.CharField(max_length=200)
    
    def __str__(self):
        return '%s %s %s %s %s' % (self.title, self.grade, self.type_donnees, self.indices, self.commentary)
        
class Correction(models.Model):
    exercise = models.ForeignKey(Exercise)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)