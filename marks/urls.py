from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('marks/', views.get_marks),
]
