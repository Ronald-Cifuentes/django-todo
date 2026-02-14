from django.urls import path
from . import views

urlpatterns = [
    path('todos', views.todo_list, name='todo-list'),
    path('todos/<str:id>', views.todo_detail, name='todo-detail'),
]
