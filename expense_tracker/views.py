from django.shortcuts import redirect, render
from forms import LoginForm, RegisterForm
from api.users import UserApi as api
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from forms import RegisterForm


def index(request):
    return render(request, "index.html")

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'register.html', {'form': form})