from django.db import models
from django.contrib.auth.models import User



from teachers.models import Teacher, Chapter
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
    
    author = models.ForeignKey('Teacher', related_name="courses")
    chapter = models.ForeignKey('Chapter', related_name="courses")
    favorites = models.ManyToManyField(User, related_name="favorite_courses", blank=True, null=True)
    # videos = models.ManyToManyField(Video)
    # images = models.ManyToManyField(Image)
    # definitions = models.ManyToManyField(Definition)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.name

    def total_pages(self):
        return self.pages.count()


class Page(models.Model):
    name = models.CharField(max_length=30)
    order = models.IntegerField()
    
    course = models.ForeignKey(Course, related_name="pages")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.name

class Section(models.Model):
    name = models.CharField(max_length=30)
    markdown_content = models.TextField(default="")
    html_content = models.TextField(blank=True)
    order = models.IntegerField()
    
    page = models.ForeignKey(Page, related_name="sections")
    
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

class Skill(models.Model):
    # max_length=200 me paraît un peu beaucoup ... (tout ceci prend de la place
    # inutilement dans la base de données
    short_name = models.CharField(max_length=30)
    
    # http://stackoverflow.com/questions/7354588/django-charfield-vs-textfield
    description = models.CharField(max_length=200)
    
    chapter = models.ManyToManyField('Chapter')
    
#
# all about exercise
#
class Exercise_type(models.Model):
    title = models.CharField(max_length=20)
    donnees = models.CharField(max_length=50)
    user = models.ManyToManyField('Student')
    skill = models.ManyToManyField(Skill)
    
    

class Exercise(models.Model):
    user = models.ManyToManyField('Student')
    
    # ceci veut dire qu'il n'y a forcément qu'un seul prof par exercice. C'est
    # un choix, mais il faudrait alors une option de partage qui permettrait de
    # partager un exercice avec d'autres profs coauteurs
    owner = models.ForeignKey('Teacher')
    
    # éventuellement rajouter un champ "collaborateurs"
    
    chapter = models.ManyToManyField('teachers.Chapter')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    num_exercise = models.IntegerField()
    grade = models.CharField(max_length=60)
    type_donnees = models.ForeignKey(Exercise_type)
    
    # essaye de garder une certaine cohérence (anglais / français) ... et cherche
    # le mot anglais (et également singulier / pluriel). Ce champ va stocker UN indice et non plusieurs
    # Ne peut-on pas imaginer plusieurs indices par exercice (il faudrait alors une FK vers une autre table
    indices = models.CharField(max_length=50)
    
    # j'appellerais ce champ plutôt "comment"
    commentary = models.CharField(max_length=200)
    
    def __str__(self):
        return '%s %s %s %s %s' % (self.title, self.grade, self.type_donnees, self.indices, self.commentary)
        
# définir une nouvelle table "Hint" (indices) ==> un exo peut avoir plusieures indices.
# Il faudrait pouvoir ordonner les indices pour un certain exercice

'''

attention à faire la différence entre un indice qui concerne tout un type d'exercice
et un indice qui concerne un exercice particulier. (dexu tables différentes)

'''
        
class Correction(models.Model):
    exercise = models.ForeignKey(Exercise)
    
    # je pense qu'en anglais, on dit plutôt "created_on", "updated_on"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Quiz(models.Model): #Infos générales sur le quiz
    title = models.CharField(max_length=100)
    
    # DONC : il faudrait initialiser ce champ avec la date actuelle, car cette 
    # date est normalement égale à la date à laquelle l'instance est créée
    # dans une vue. Je mettrais plutôt un DateTimeField, car il est parfois
    # utile de connaitre l'heure de création...
    creation_date = models.DateField()
    code = models.CharField(max_length=1000) #Format texte du quiz
    id_prof = models.ForeignKey('Teacher')
    
    # DONC : je ne suis pas très convaincu par cette ForeignKey, car cela implique qu'un
    # quiz est nécessairemement rattaché à un seul chapitre. Il faudrait plutôt 
    # une relation nc-nc à mon sens.
    id_chapter = models.ForeignKey('Chapter')
    
    # DONC : il manque probablement une relation ManyToMany vers Student à travers
    # la table CompletedQuiz qui ferait office de table de jonction
    
class CompletedQuiz(models.Model): #Tentative de réponse au quiz par un élève
    submit_date = models.DateField()
    id_quiz = models.ForeignKey(Quiz) #Relation avec le quiz complété
    id_student = models.ForeignKey('Student')

#    
#Classes abstraites
#

class QuizQuestion(models.Model): #Classe abstraite dont héritent toutes les questions
    text = models.CharField(max_length=200) #Énoncé
    comment = models.CharField(max_length=200) #Commentaire affiché lors de la correction
    
    # DONC : il faudrait trouver un moyen pour qu'il soit garranti qu'il n'y ait
    # jamais deux questions avec le même numéro dans le même quiz (peut-on imposer
    # cette contrainte avec la définition des modèles Django ???)
    # indication : http://stackoverflow.com/questions/4522648/unique-foreign-key-pairs-with-django
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
    submitted_quiz = models.ForeignKey(CompletedQuiz) #Relation vers la tentative
    
class Teacher(Student):
    pass

class Group(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ManyToManyField(Teacher)
    student = models.ManyToManyField('Student')
    
#
#  Classification
#
class Theme(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
      return self.name

class Chapter(models.Model):
    name = models.CharField(max_length=30)

    theme = models.ForeignKey(Theme, related_name="chapters")

    def __str__(self):
      return self.name

class Student(User):
    done_skills = models.ManyToManyField('Skill')
    
    def __str__(self):
        return '%s %s' % (self.prenom, self.nom)