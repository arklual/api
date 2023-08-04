from django.db import models
from subjects.models import Subject
from accounts.models import Account

class Homework(models.Model):
    subject = models.ForeignKey(Subject, models.CASCADE, verbose_name='Предмет')
    task = models.TextField('Задание')
    deadline = models.DateField('Срок сдачи', blank=True)
    is_done = models.BooleanField(verbose_name='Сделано?', default=False)
    user = models.ForeignKey(Account, models.CASCADE, verbose_name='Ученик')

    def __str__(self) -> str:
        return self.subject.name + ', ' + self.user.last_name

class HomeworkAttachment(models.Model):
    file = models.FileField('Файл')
    homework = models.ForeignKey(Homework, models.CASCADE, verbose_name='Домашнее задание')