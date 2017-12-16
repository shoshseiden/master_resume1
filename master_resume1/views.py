from django.contrib.auth.models import User

import account.forms
import account.views

import master_resume1.forms

class SignupView(account.views.SignupView):

    form_class = master_resume1.forms.SignupForm
    identifier_field = "email"

    def after_signup(self, form):
        self.create_profile(form)
        super(SignupView, self).after_signup

    def create_profile(self, form):
        profile = self.created_user.profile # replace with your reverse one-to-one profile attribute
        profile.phone = form.cleaned_data["phone"]
        profile.street_address = form.cleaned_data["street_address"]
        profile.city = form.cleaned_data["city"]
        profile.state = form.cleaned_data["state"]
        profile.zip_code = form.cleaned_data["zip_code"]
        profile.save()

    def generate_username(self, form):
        # Do something to generate a unique username (required by the django user model)
        username = User.email
        return username

class LoginView(account.views.LoginView):

    form_class = account.forms.LoginEmailForm
