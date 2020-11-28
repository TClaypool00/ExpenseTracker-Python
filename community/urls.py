from django.urls import path
from . import views

urlpatterns = [
    path('home', views.community_index),
    path('posts/create', views.create_post),
    path('posts/details/<int:id>', views.post_details)
]