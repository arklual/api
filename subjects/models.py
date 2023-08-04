from django.db import models

class Subject(models.Model):
    name = models.CharField(verbose_name='Предмет', max_length=200)
    id = models.IntegerField(verbose_name='ID', primary_key=True)

    def __str__(self):
        return self.name