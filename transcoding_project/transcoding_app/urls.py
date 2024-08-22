# transcoding_app/urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
   
    path('', views.home, name='home'),  # Página de inicio
    path('upload/', views.upload_video, name='upload_video'),  
    path('videos/', views.video_list, name='video_list'), 
    path('videos/<int:video_id>/', views.video_detail, name='video_detail'),  
   
    ]