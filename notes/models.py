from django.db import models
from subjects.models import Subject
from accounts.models import Account
from datetime import datetime



class Note(models.Model):
    subject = models.ForeignKey(Subject, models.CASCADE, verbose_name='Предмет')
    author = models.ForeignKey(Account, models.CASCADE, verbose_name="Автор конспекта", null=True)
    date = models.DateField(verbose_name='Дата конспекта', default=datetime.today())

class NotePhoto(models.Model):
    photo = models.FileField('Фото')
    note = models.ForeignKey(Note, models.CASCADE, verbose_name='Конспект')