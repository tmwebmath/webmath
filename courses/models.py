from django.db import models
from django.contrib.auth.models import User
from teachers.models import Teacher

#
# Course build
#
class Course(models.Model):
  name = models.CharField(max_length=30, unique=True)
  description = models.TextField()
  difficulty = models.IntegerField

  author = models.ForeignKey(Teacher)
  chapter = models.ForeignKey(Chapter)
  favorites = models.ManyToManyField(User)
  # videos = models.ManyToManyField(Video)
  # images = models.ManyToManyField(Video)
  # definitions = models.ManyToManyField(Definition)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Page(models.Model):
  name = models.CharField(max_length=30)
  content = models.TextField()
  order = models.IntegerField()

  course = models.ForeignKey(Course)

class Section(models.Model)
  name = models.CharField(max_length=30)
  content = models.TextField()
  order = models.IntegerField()

  page = models.ForeignKey(Page)

#
# Course organization
#
class Theme(models.Model):
  name = models.CharField(max_length=30)

class Chapter(models.Model):
  name = models.CharField(max_length=30)

  theme = models.ForeignKey(Theme)

#
# User functionalities
#
class Comment(models.Model):
  content = models.TextField()

  user = models.ForeignKey(User)
  course = models.ForeignKey(Course)
  section = models.ForeignKey(Section)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Request(models.Model):
  name = models.CharField(max_length=30)
  content = models.TextField()

  user = models.ForeignKey(User)

class Progression(models.Model):
  page = models.ForeignKey(Page)
  status = models.ForeignKey(Status)
  user = models.ForeignKey(User)

class Status(models.Model):
  name = models.CharField(max_length=30, unique=True)

#
# Various
#
class Definition(models.Model):
  word = models.CharField(max_length=20)
  definition = models.TextField()

class Video(models.Model):
  pass

class Image(models.Model):
  pass