from django.db import models
from subjects.models import Subject

class Marks(models.Model):
    value = models.IntegerField(verbose_name='Оценка')
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE, verbose_name='Предмет')
    
