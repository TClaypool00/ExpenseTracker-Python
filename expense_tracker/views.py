from django.shortcuts import redirect, render
from forms import LoginForm, RegisterForm
from django.contrib.auth import views as auth_views
from forms import RegisterForm
from django.contrib.auth.decorators import login_required
from api import bills, loan

@login_required()
def index(request):
    user_id = request.user.userid
    user_bills = bills.BillsApi.get_all_bills_by_user_id(request, user_id)
    user_loans = loan.LoanApi.get_loan_by_user_id(request, user_id)
    
    return render(request, "index.html", {'bills' : user_bills, 'loans' : user_loans})


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