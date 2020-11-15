from django.shortcuts import render, redirect
from forms import CreateStoreForm
from api.stores import StoreApi as api
from api.api import Api as base
from django.contrib.auth.decorators import login_required

@login_required()
def create(request):
    if request.method == 'POST':
        form = CreateStoreForm(request.POST)
        if form.is_valid():
            store_name = form.cleaned_data['store_name']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            post_code = form.cleaned_data['zip']
            phone_num = form.cleaned_data['phone_num']
            email = form.cleaned_data['email']
            website = form.cleaned_data['website']
            is_credit_union = form.cleaned_data['is_credit_union']
            
            if post_code == None:
                post_code = 0
            if phone_num == None:
                phone_num = 0
            
            api.create_store(base, store_name, address, city, state, post_code, phone_num, email, website, is_credit_union)
            
            return redirect('/')
    else:
        form = CreateStoreForm()
        return render(request, 'create_store.html', {'form' : form})