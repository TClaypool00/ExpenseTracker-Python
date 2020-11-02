from django.shortcuts import redirect, render
from forms import LoginForm, RegisterForm
from django.contrib.auth import views as auth_views
from forms import RegisterForm
from django.contrib.auth.decorators import login_required

@login_required()
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