from django.shortcuts import render, redirect
from forms import CreateBillForm
from api.bills import BillsApi as api
from api.stores import StoreApi as stores
from django.contrib.auth.decorators import login_required

@login_required()
def create(request):
    store_list = stores.get_all_stores(stores, is_credit_union=False)
    if request.method == 'POST':
        form = CreateBillForm(request.POST)
        if form.is_valid():
            bill_name = form.cleaned_data['bill_name']
            bill_date = form.cleaned_data['bill_date']
            bill_price = form.cleaned_data['bill_price']
            is_late = form.cleaned_data['is_late']
            user = request.user
            store_id = request.POST.get('storeList', 1)
            
            api.create_bill(request, bill_name, bill_date, bill_price, is_late, store_id, user.userid)
            
            return redirect('/')
    else:
        form = CreateBillForm()
        return render(request, 'create_bill.html', {'form': form, 'stores': store_list})