from django.db import models
from subjects.models import Subject

class Testwork(models.Model):
    subject = models.ForeignKey(Subject, models.CASCADE, verbose_name='Предмет')
    date = models.DateField('Срок сдачи', blank=True)
    topic = models.CharField('Тема', max_length=220)
    type = models.CharField('Тип работы', max_length=50)

    def __str__(self) -> str:
        return self.subject.name +' '+str(self.date)