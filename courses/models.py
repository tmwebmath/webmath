from django.db import models
from django.contrib.auth.models import User

#
# Status progressions
#
class Status(models.Model):
    name = models.CharField(max_length=30, unique=True)

#
# Course build
#
class Course(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    difficulty = models.IntegerField()
    
    author = models.ForeignKey('teachers.Teacher')
    chapter = models.ForeignKey('teachers.Chapter')
    favorites = models.ManyToManyField(User, related_name="favorite_courses")
    # videos = models.ManyToManyField(Video)
    # images = models.ManyToManyField(Image)
    # definitions = models.ManyToManyField(Definition)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Page(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField()
    order = models.IntegerField()
    
    course = models.ForeignKey(Course)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Section(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField()
    order = models.IntegerField()
    
    page = models.ForeignKey(Page)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#
# User functionalities
#
class CourseComment(models.Model):
    content = models.TextField()
    
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    section = models.ForeignKey(Section)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CourseRequest(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField()
    
    user = models.ForeignKey(User)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Progression(models.Model):
    page = models.ForeignKey(Page)
    status = models.ForeignKey(Status)
    user = models.ForeignKey(User)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#
# Various
#
class Definition(models.Model):
    word = models.CharField(max_length=20)
    definition = models.TextField()

class Video(models.Model):
    video = models.FileField(upload_to="courses/static/courses/uploads/videos/")

class Image(models.Model):

    def imagename(instance, filename):
        return "/courses/static/courses/uploads/images/"

    image = models.ImageField(upload_to="courses/static/courses/uploads/images/")
