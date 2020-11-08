from django.shortcuts import render, redirect
from forms import CreateMiscForm
from api.misc import MiscApi as api
from api.stores import StoreApi as store
from datetime import date
from django.contrib.auth.decorators import login_required

@login_required()
def create(request):
    store_list = store.get_all_stores(store, is_credit_union=False)
    if request.method == 'POST':
        form = CreateMiscForm(request.POST)
        if form.is_valid():
            misc_name = form.cleaned_data['misc_name']
            memo = form.cleaned_data['memo']
            price = form.cleaned_data['price']
            user_id = request.user.userid
            store_id = request.POST.get('storeList', 1)
            cur_date = date.today()
            
            api.create_misc(api, price, store_id, cur_date, user_id, memo, misc_name)
            
            return redirect('/')
    else:
        form = CreateMiscForm()
        return render(request, 'create_misc.html', {'form' : form, 'stores' : store_list})