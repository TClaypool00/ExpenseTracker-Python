from django.shortcuts import redirect, render
from api.budgets import BudgetApi as api
from django.contrib.auth.decorators import login_required

@login_required()
def edit_budget(request):
    user_id = request.user.userid
    user_budget = api.get(api, user_id, budget_id=None)
    CONTEXT = {'budget' : user_budget}
    
    if request.method == 'POST':
        savings = request.POST.get('savings', 0)
        
        api.update_budget(api, user_id, savings, 'budget.budgetId')
        
        return redirect('/')
    else:
        return render(request, 'edit_budget.html', CONTEXT)