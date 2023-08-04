from django.db import models
from subjects.models import Subject

class Note(models.Model):
    subject = models.ForeignKey(Subject, models.CASCADE, verbose_name='Предмет')

class NotePhoto(models.Model):
    photo = models.FileField('Фото')
    note = models.ForeignKey(Note, models.CASCADE, verbose_name='Конспект')