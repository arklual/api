from django.db import models
from subjects.models import Subject

class Homework(models.Model):
    subject = models.ForeignKey(Subject, models.CASCADE, verbose_name='Предмет')
    task = models.TextField('Задание')

class HomeworkFile(models.Model):
    file = models.FileField('Файл')
    homework = models.ForeignKey(Homework, models.CASCADE, verbose_name='Домашнее задание')