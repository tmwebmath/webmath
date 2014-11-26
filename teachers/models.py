from django.db import models
from django.contrib.auth.models import User

class Teacher(User):
    e_mail = models.CharField(max_length=30)
