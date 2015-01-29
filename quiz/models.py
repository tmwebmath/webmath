from django.db import models

# Create your models here.
# Commentaire vraiment inutile

class Quiz(models.Model): #Infos générales sur le quiz
    title = models.CharField(max_length=100)
    
    # DONC : il faudrait initialiser ce champ avec la date actuelle, car cette 
    # date est normalement égale à la date à laquelle l'instance est créée
    # dans une vue. Je mettrais plutôt un DateTimeField, car il est parfois
    # utile de connaitre l'heure de création...
    creation_date = models.DateField()
    code = models.CharField(max_length=1000) #Format texte du quiz
    id_prof = models.ForeignKey('teachers.Teacher')
    
    # DONC : je ne suis pas très convaincu par cette ForeignKey, car cela implique qu'un
    # quiz est nécessairemement rattaché à un seul chapitre. Il faudrait plutôt 
    # une relation nc-nc à mon sens.
    id_chapter = models.ForeignKey('teachers.Chapter')
    
    # DONC : il manque probablement une relation ManyToMany vers Student à travers
    # la table CompletedQuiz qui ferait office de table de jonctionqreqrewqrewqrewqrweqrewqwerwqerqwerwqrewqerqwerwqerqwerwqerwqerqwrwqer qwer
    
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