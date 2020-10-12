from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    email = forms.EmailField(label="Email Address")
    password = forms.CharField(label="Password")
    is_admin = forms.BooleanField(label="Are you an admin?")
    phone_num = forms.IntegerField(label="Phone number")
    salary = forms.FloatField(label="Salary")