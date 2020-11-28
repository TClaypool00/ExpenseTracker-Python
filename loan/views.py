from api.loan import LoanApi
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from api import stores, loan
from forms import CreateLoanForm
from api.budgets import BudgetApi
from api.api import Api
from datetime import date

@login_required()
def create(request):
    user_id = request.user.userid
    store_list = stores.StoreApi.get_all_stores(stores.StoreApi, is_credit_union=True)
    form = CreateLoanForm()
    user_budget = BudgetApi.get(BudgetApi, user_id, budget_id=None)
    CONTEXT = {'form': form, 'stores' : store_list, 'budget' : user_budget}
    if request.method == 'POST':
        form = CreateLoanForm(request.POST)
        if form.is_valid():
            loan_name = form.cleaned_data['loan_name']
            due_date = request.POST.get('duDate', date.today())
            deposit = form.cleaned_data['deposit']
            monthly_amt_due = form.cleaned_data['monthly_amt_due']
            total_amt_due = form.cleaned_data['total_amt_due']
            store_id = request.POST.get('storeList', 1)
            
            loan.LoanApi.create_loan(loan.LoanApi, loan_name, str(due_date), monthly_amt_due, deposit, total_amt_due, store_id, user_id)
            if user_budget is not None:
                BudgetApi.update_budget(Api, user_id, user_budget['savingsMoney'], user_budget['budgetId'])
            
            return redirect('/')
    else:
        return render(request, 'create_loan.html', CONTEXT)
    
    
@login_required()
def loan_details(request, id):
    loan = LoanApi.get_by_id(Api, id)
    
    return render(request, 'loan_details.html', {'loan' : loan})