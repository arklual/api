# Generated by Django 4.0.10 on 2023-09-24 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, verbose_name='Срок сдачи')),
                ('topic', models.CharField(max_length=220, verbose_name='Тема')),
                ('type', models.CharField(max_length=50, verbose_name='Тип работы')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.subject', verbose_name='Предмет')),
            ],
        ),
    ]
