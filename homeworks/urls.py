from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddHomework.as_view()),
    path('get/', views.GetHomeworks.as_view()),
    path('change-done/', views.ChangeHomeworkDone.as_view()),
]
