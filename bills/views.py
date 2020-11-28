from django.shortcuts import render, redirect
from forms import CreateBillForm
from api.bills import BillsApi as api
from api.stores import StoreApi as stores
from django.contrib.auth.decorators import login_required
from api.budgets import BudgetApi
from api.api import Api
from datetime import date

@login_required()
def create(request):
    store_list = stores.get_all_stores(stores, is_credit_union=False)
    user_id = request.user.userid
    user_budget = BudgetApi.get(BudgetApi, user_id, budget_id=None)
    form = CreateBillForm()
    CONTEXT = {'budget' : user_budget, 'form': form, 'stores': store_list}
    if request.method == 'POST':
        form = CreateBillForm(request.POST)
        if form.is_valid():
            bill_name = form.cleaned_data['bill_name']
            bill_date = request.POST.get('dueDate', date.today())
            bill_price = form.cleaned_data['bill_price']
            is_late = form.cleaned_data['is_late']
            store_id = request.POST.get('storeList', 1)
            
            api.create_bill(request, bill_name, str(bill_date), bill_price, is_late, store_id, user_id)
            if user_budget is not None:
                BudgetApi.update_budget(Api, user_id, user_budget['savingsMoney'], user_budget['budgetId'])
            
            return redirect('/')
    else:
        return render(request, 'create_bill.html', CONTEXT)
    
    
@login_required()
def bill_details(request, id):
    bill = api.get_by_id(api, id)
    
    return render(request, 'bill_details.html', {'bill' : bill})