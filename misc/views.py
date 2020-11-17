from django.shortcuts import render, redirect
from forms import CreateMiscForm
from api.misc import MiscApi as api
from api.stores import StoreApi as store
from django.contrib.auth.decorators import login_required
from api.budgets import BudgetApi
from api.api import Api

@login_required()
def create(request):
    store_list = store.get_all_stores(store, is_credit_union=False)
    user_id = request.user.userid
    form = CreateMiscForm()
    user_budget = BudgetApi.get(BudgetApi, user_id, budget_id=None)
    CONTEXT = {'form' : form, 'stores' : store_list, 'budget' : user_budget}
    
    if request.method == 'POST':
        form = CreateMiscForm(request.POST)
        if form.is_valid():
            misc_name = form.cleaned_data['misc_name']
            memo = form.cleaned_data['memo']
            price = form.cleaned_data['price']
            store_id = request.POST.get('storeList', 1)
            
            api.create_misc(api, price, store_id, user_id, memo, misc_name)
            if user_budget is not None:
                BudgetApi.update_budget(Api,user_id, 'budget.savingsMoney', 'budget.budgetId')
            
            return redirect('/')
    else:
        return render(request, 'create_misc.html', CONTEXT)
    
    
@login_required()
def misc_details(request, id):
    misc = api.get_misc_by_id(api, id)
    
    return render(request, 'misc_details.html', {'misc' : misc})