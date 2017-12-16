from django import forms
import account.forms

class SignupForm(account.forms.SignupForm):
    phone = forms.CharField()
    street_address = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zip_code = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]
