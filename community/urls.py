from django.urls import path
from . import views

urlpatterns = [
    path('home', views.community_index),
    path('posts/create', views.create_post),
]