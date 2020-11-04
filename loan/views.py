from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from api import stores, loan
from forms import CreateLoanForm

@login_required()
def create(request):
    if request.method == 'POST':
        form = CreateLoanForm(request.POST)
        if form.is_valid():
            loan_name = form.cleaned_data['loan_name']
            due_date = form.cleaned_data['due_date']
            deposit = form.cleaned_data['deposit']
            monthly_amt_due = form.cleaned_data['monthly_amt_due']
            total_amt_due = form.cleaned_data['total_amt_due']
            user_id = str(request.user.userid)
            store_id = request.POST.get('storeList', 1)
            
            loan.LoanApi.create_loan(loan.LoanApi, loan_name, due_date, monthly_amt_due, deposit, total_amt_due, store_id, user_id)
            
            return redirect('/')
    else:
        store_list = stores.StoreApi.get_all_stores(request)
        form = CreateLoanForm()
        return render(request, 'create_loan.html', {'form': form, 'stores' : store_list})