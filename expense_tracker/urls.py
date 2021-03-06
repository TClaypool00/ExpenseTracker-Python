"""expense_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import users
from django.contrib import admin
from django.urls import include, path
import users.views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('register/', views.register),
    path('', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('bills/', include('bills.urls')),
    path('loan/', include('loan.urls')),
    path('misc/', include('misc.urls')),
    path('store/', include('store.urls')),
    path('subscription/', include('subscription.urls')),
    path('myBudget/', include('budget.urls')),
    path('logout/', views.logout_user),
    path('update-password/', views.change_password),
    path('community/', include('community.urls')),
    path('myCalendar/', include('cal.urls')),
]
