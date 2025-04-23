from django.urls import path
from . import views

app_name = 'media_uploads'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
]