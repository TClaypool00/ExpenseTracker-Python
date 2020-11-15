from django.forms.widgets import EmailInput, HiddenInput, NumberInput, TextInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms

DUE_DATE = {'placeholder' : 'Due Date'}

class RegisterForm(UserCreationForm):
    firstname = forms.CharField(widget=TextInput(attrs={'placeholder': 'First Name'}), label=False)
    lastname = forms.CharField(widget=TextInput(attrs={'placeholder': 'Last Name'}), label=False)
    email = forms.EmailField(widget=TextInput(attrs={'placeholder': 'Email Address'}), label=False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label=False)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Comfirm Password'}), label=False)
    phonenum = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}), label=False)
    salary = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Monthly Salary'}), label=False)
    
    class Meta:
        model = get_user_model()
        fields = ('firstname', 'lastname', 'email', 'password1', 'password2', 'phonenum', 'salary')
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder' : 'Email Address'}), label=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label=False)
    

class CreateBillForm(forms.Form):
    bill_name = forms.CharField(widget=TextInput(attrs={'placeholder': 'Bill Nickname'}), label=False)
    bill_date = forms.CharField(widget=TextInput(attrs=DUE_DATE), label=False)
    bill_price = forms.FloatField(widget=NumberInput(attrs={'placeholder': 'Price of Bill'}), label=False)
    is_late = forms.BooleanField(required=False, widget=HiddenInput)
    

class CreateLoanForm(forms.Form):
    loan_name = forms.CharField(widget=TextInput(attrs={'placeholder' : 'Loan Nickname'}), label=False)
    due_date = forms.CharField(widget=TextInput(attrs=DUE_DATE), label=False)
    deposit = forms.FloatField(widget=NumberInput(attrs={'placeholder': 'Deposit'}), label=False)
    monthly_amt_due = forms.FloatField(widget=NumberInput(attrs={'placeholder': 'Monthly Amount Due'}), label=False)
    total_amt_due = forms.FloatField(widget=NumberInput(attrs={'placeholder': 'Total Amount Due'}), label=False)
    
class CreateStoreForm(forms.Form):
    store_name = forms.CharField(widget=TextInput(attrs={'placeholder' : 'Store Name'}), label=False)
    address = forms.CharField(widget=TextInput(attrs={'placeholder' : 'Street Address'}), label=False, required=False)
    city = forms.CharField(widget=TextInput(attrs={'placeholder' : 'City'}), label=False, required=False)
    state = forms.CharField(widget=TextInput(attrs={'placeholder' : 'MO'}), label=False, required=False)
    zip = forms.IntegerField(widget=NumberInput(attrs={'placeholder' : 'Postal Zip Code'}), label=False, required=False)
    phone_num = forms.IntegerField(widget=NumberInput(attrs={'placeholder' : 'Customer Service Phone Number'}), label=False, required=False)
    email = forms.EmailField(widget=EmailInput(attrs={'placeholder': 'Customer Service Email'}), label=False, required=False)
    website = forms.CharField(widget=TextInput(attrs={"placeholder" : "Company's Website"}), label=False)
    is_credit_union = forms.BooleanField(label='Is this a Credit Union', required=False)
    
    
class CreateMiscForm(forms.Form):
    misc_name = forms.CharField(widget=TextInput(attrs={'placeholder' : 'Name'}), label=False)
    price = forms.FloatField(widget=NumberInput(attrs={'placeholder': 'Price'}), label=False)
    memo = forms.CharField(widget=TextInput(attrs={'placeholder' : 'Memo (Optional)'}), label=False, required=False)
    
    
class CreateSubForm(forms.Form):
    sub_name = forms.CharField(widget=TextInput(attrs={'placeholder' : 'Name'}), label=False)
    due_date = forms.CharField(widget=TextInput(attrs=DUE_DATE), label=False)
    price = forms.FloatField(widget=NumberInput(attrs={'placeholder' : 'Price'}), label=False)