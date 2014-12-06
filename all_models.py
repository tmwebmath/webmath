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

    def filename(instance, filename):
        return "/courses/static/courses/uploads/videos/{}/{}".format(instance.pk, filename)

    video = models.FileField(upload_to=filename)

class Image(models.Model):

    def filename(instance, filename):
        return "/courses/static/courses/uploads/images/{}/{}".format(instance.pk, filename)

    image = models.ImageField(upload_to=filename)
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
    updated_at = models.DateTimeField(auto_now=True)from django.db import models

# Create your models here.

class Quiz(models.Model): #Infos générales sur le quiz
    title = models.CharField(max_length=100)
    creation_date = models.DateField()
    #code = models.CharField(max_length=1000) #Format texte du quiz
    id_prof = models.ForeignKey('teachers.Teacher')
    id_chapter = models.ForeignKey('teachers.Chapter')
    
class CompletedQuiz(models.Model): #Tentative de réponse au quiz par un élève
    submit_date = models.DateField()
    id_quiz = models.ForeignKey(Quiz) #Relation avec le quiz complété
    id_student = models.ForeignKey('students.Student')

#    
#Classes abstraites
#

class QuizQuestion(models.Model): #Classe abstraite dont héritent toutes les questions
    text = models.CharField(max_length=200) #Énoncé
    comment = models.CharField(max_length=200) #Commentaire affiché lors de la correction
    number = models.IntegerField() #Ordre de la question dans le quiz
    id_quiz = models.ForeignKey(Quiz)
    
    class Meta:
        abstract = True

#
#Tables concernant les questions simples
#
        
class SimpleQuestion(QuizQuestion):
    pass

class SqAnswer(models.Model): #Les réponses correctes
    text = models.CharField(max_length=50)
    question = models.ForeignKey(SimpleQuestion) #Relation vers la question

class SqSubmit(models.Model): #Réponse soumise par un élève
    text = models.CharField(max_length=50)
    question = models.ForeignKey(SimpleQuestion) #Relation vers la question à laquelle l'élève a répondu
    submitted_quiz = models.ForeignKey(CompletedQuiz) #Relation vers la tentative

#    
#Tables concernant les QCM
#

class Qcm(QuizQuestion):
    multi_answers = models.BooleanField() #True si il est possible de cocher plusieurs choix
    show_list = models.BooleanField() #True si les choix sont affichés sous forme de liste déroulante
    
class QcmChoice(models.Model): #Choix affichés pour un QCM
    text = models.CharField(max_length=50)
    valid = models.BooleanField() #Vaut True si la case doit être cochée
        
class QcmSubmit(models.Model): #Choix sélectionnés par l'élève dans un QCM
    submitted_quiz = models.ForeignKey(CompletedQuiz) #Relation vers la tentativefrom django.db import models
from django.contrib.auth.models import User

class Student(User):
    done_skills = models.ManyToManyField('exercises.Skill')
    
    def __str__(self):
        return '%s %s' % (self.prenom, self.nom)from django.db import models
from django.contrib.auth.models import User

class Teacher(User):
    pass

class Group(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ManyToManyField(Teacher)
    student = models.ManyToManyField('students.Student')
    
#
#  Classification
#
class Theme(models.Model):
    name = models.CharField(max_length=30)

class Chapter(models.Model):
    name = models.CharField(max_length=30)

    theme = models.ForeignKey(Theme)