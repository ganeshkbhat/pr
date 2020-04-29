from django.db import models
from django.conf import settings

# https://stackoverflow.com/questions/20190809/django-one-to-many-to-many-relationships-admin
# https://stackoverflow.com/questions/24890269/django-inline-formset-with-model-subclasses-or-just-multiple-models

# Create your models here.

class Question(models.Model):
    question = models.CharField("Question")
    # needed inline but for this but one-to-many in inline doesnt work
    # Does it work
    # answer = models.ForeignKey(...need OneToMany relationship to tests.question...)
    # DJANGO DOESNT OFFICIALLY SUPPORT THIS

 
class Answers(models.Model):
    answer = models.ForeignKey(Question, on_delete=models.PROTECT)

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='username')
    assigned_question = models.ForeignKey(Answers, on_delete=models.PROTECT)


class QuestionsAnswered(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='username')
    # question number
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    answer = models.CharField("Answer seleted")
    # selected answer
    selected_answer = models.BoolField("Selected Answer")

