from django import forms

class SignupForm(account.forms.SignupForm):
    phone = forms.CharField()
    street_address = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zip_code = form.IntegerField()
