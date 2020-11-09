from django.shortcuts import render, redirect
from forms import CreateSubForm
from api.subs import SubsApi as api
from api.stores import StoreApi as stores
from django.contrib.auth.decorators import login_required

@login_required()
def create(request):
    store_list = stores.get_all_stores(stores, is_credit_union=False)
    if request.method == 'POST':
        form = CreateSubForm(request.POST)
        if form.is_valid():
            sub_name = form.cleaned_data['sub_name']
            due_date = form.cleaned_data['due_date']
            price = form.cleaned_data['price']
            user_id = request.user.userid
            store_id = request.POST.get('storeList', 1)
            
            api.create_sub(api, due_date, price, store_id, sub_name, user_id)
            
            return redirect('/')
    else:
        form = CreateSubForm()
        CONTEXT = {'form' : form, 'stores' : store_list}
        return render(request, 'create_sub.html', CONTEXT)