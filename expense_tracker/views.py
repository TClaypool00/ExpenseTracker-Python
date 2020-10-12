from django.shortcuts import redirect, render
from users.create import RegisterForm
from api.users import UserApi as api


def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            is_admin = form.cleaned_data['is_admin']
            phone_num = form.cleaned_data['phone_num']
            salary = form.cleaned_data['salary']
            
            api.create_user(request,first_name, last_name, email, password, is_admin, phone_num, salary)
            
            return redirect('/login')
    else:
        form = RegisterForm()
        return render(request, "register.html", {"form": form})
    