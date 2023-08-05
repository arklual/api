from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('marks/', views.GetMarks.as_view()),
]
