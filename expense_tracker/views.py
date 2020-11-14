from django.shortcuts import redirect, render
from forms import LoginForm, RegisterForm
from django.contrib.auth import views as auth_views
from forms import RegisterForm
from django.contrib.auth.decorators import login_required
from api import api
from api.loan import loan_url
from api.bills import bill_url
from api.subs import sub_url
from api.misc import misc_url
from api.budgets import budget_url

@login_required()
def index(request):
    user_id = request.user.userid
    user_bills = api.Api.get_all(api, bill_url, user_id)
    user_loans = api.Api.get_all(api, loan_url, user_id)
    user_subs = api.Api.get_all(api, sub_url, user_id)
    user_misc = api.Api.get_all(api, misc_url, user_id)
    user_budget = api.Api.get_all(api, budget_url, user_id)
    
    CONTEXT = {'bills' : user_bills, 'loans' : user_loans, 'subs' : user_subs, 'miscs' : user_misc, 'budget' : user_budget}
    
    return render(request, "index.html", CONTEXT)


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    return render(request, 'register.html', {'form': form})