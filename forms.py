from django import forms
from django.forms.widgets import NumberInput, PasswordInput, TextInput

class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=TextInput(attrs={'placeholder' : 'First Name'}), label=False)
    last_name = forms.CharField(widget=TextInput(attrs={'placeholder' : 'Last Name'}), label=False)
    email = forms.EmailField(widget=TextInput(attrs={'placeholder' : 'Email Address'}), label=False)
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder' : 'Password'}), label=False)
    comfirm_password = forms.CharField(widget=PasswordInput(attrs={"placeholder": "Comfirm Password"}), label=False)
    is_admin = forms.BooleanField(label=False, required=False, widget=forms.HiddenInput)
    phone_num = forms.IntegerField(widget=NumberInput(attrs={'placeholder' : 'Phone Number'}), label=False)
    salary = forms.FloatField(widget=NumberInput(attrs={'placeholder' : 'Monthly Salary'}), label=False)
    
class LoginForm(forms.Form):
    email = forms.EmailField(widget=TextInput(attrs={'placeholder' : 'Email Address'}), label=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label=False)