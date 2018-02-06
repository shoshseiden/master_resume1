from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views import generic

from master_resume1.models import Profile, Skill

import account.forms
import account.views

import master_resume1.forms


class SignupView(account.views.SignupView):

    form_class = master_resume1.forms.SignupForm
    identifier_field = "email"

    def after_signup(self, form):
        self.create_profile(form)
        super(SignupView, self).after_signup(form)

    def create_profile(self, form):
        profile = self.created_user.profile
        profile.first_name = form.cleaned_data["first_name"]
        profile.last_name = form.cleaned_data["last_name"]
        profile.phone = form.cleaned_data["phone"]
        profile.street_address = form.cleaned_data["street_address"]
        profile.city = form.cleaned_data["city"]
        profile.state = form.cleaned_data["state"]
        profile.zip_code = form.cleaned_data["zip_code"]
        profile.save()

    def generate_username(self, form):
        return form.cleaned_data["email"]

class LoginView(account.views.LoginView):

    form_class = account.forms.LoginEmailForm

def custom(request, profile_id):
    try:
        profile = Profile.objects.get(pk=profile_id)
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist")
    return render(request, "custom.html", {"profile": profile})

def master(request):
    '''ctx = {"skill_form": skill_form,
           "work_form": work_form,
           "education_form": education_form,
           "volunteer_form": volunteer_form}
    '''

    skill_form = SKillForm(request.POST)
    # work_form = WorkForm(request.POST)
    # education_form = EducationForm(request.POST)
    # volunteer_form = VounteerForm(request.POST)

    if request.method == "POST":
        if skill_form.is_valid():
            skill_form.save()
    else:
        pass
    return render(request, "master.html", {"skill_form": skill_form})
