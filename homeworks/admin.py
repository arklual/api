from django.contrib import admin
from homeworks.models import Homework, HomeworkAttachment

class HomeworkAttachmentInline(admin.TabularInline):
    model = HomeworkAttachment
    verbose_name = 'Приложение'
    verbose_name_plural = 'Приложения'

@admin.register(Homework)
class BookAdmin(admin.ModelAdmin):
    inlines = [HomeworkAttachmentInline]