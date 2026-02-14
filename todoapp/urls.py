"""
URL configuration for todoapp project.
"""
from django.contrib import admin
from django.urls import path, include
from todos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todos.urls')),
    path('health', views.health_check, name='health'),
]
