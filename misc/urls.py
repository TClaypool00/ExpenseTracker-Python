from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create),
    path('details/<int:id>', views.misc_details)
]