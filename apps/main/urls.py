from django.contrib import admin
from django.urls import path
from . import views
from .views import task_list
app_name = 'main'
urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/<int:id>/', views.task_edit, name='task_edit')
]
