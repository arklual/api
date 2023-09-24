from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddWork.as_view()),
    path('get/', views.GetWorks.as_view()),
]
