"""
URL configuration for todoapp project.
"""
from django.contrib import admin
from django.urls import path, include
from todos import views

urlpatterns = [
    path('', views.root, name='root'),
    path('admin/', admin.site.urls),
    path('api', views.api_root, name='api-root-no-slash'),  # /api (sin barra)
    path('api/', include('todos.urls')),
    path('health', views.health_check, name='health'),
]
