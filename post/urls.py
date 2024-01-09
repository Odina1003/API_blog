from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.getPost),
    path('post/', views.postPost),
]