from django.db import models
from subjects.models import Subject
from accounts.models import Account

class Marks(models.Model):
    user = models.ForeignKey(to=Account, on_delete=models.CASCADE, verbose_name='Студент')
    value = models.IntegerField(verbose_name='Оценка')
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE, verbose_name='Предмет')
    
