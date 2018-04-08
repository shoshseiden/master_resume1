from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views import generic

from master_resume1.forms import SignupForm, SkillForm, EducationForm, WorkForm, VolunteerForm, SkillFormSet, EducationFormSet, WorkFormSet, VolunteerFormSet
from master_resume1.models import Profile, Skill, WorkExperience, Education, VolunteerExperience

import account.forms
import account.views


class SignupView(account.views.SignupView):

    form_class = SignupForm
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
    skill_form = SkillForm()
    work_form = WorkForm()
    education_form = EducationForm()
    volunteer_form = VolunteerForm()

    ctx = {"skill_form": skill_form,
           "work_form": work_form,
           "education_form": education_form,
           "volunteer_form": volunteer_form}

    if request.method == "POST":
        skill_form = SkillForm(request.POST)
        work_form = WorkForm(request.POST)
        education_form = EducationForm(request.POST)
        volunteer_form = VolunteerForm(request.POST)

        if skill_form.is_valid():
            skill_form.save()

        if work_form.is_valid():
            work_form.save()

        if education_form.is_valid():
            education_form.save()

        if volunteer_form.is_valid():
            volunteer_form.save()
    else:
        skill_form = SkillForm()
        work_form = WorkForm()
        education_form = EducationForm()
        volunteer_form = VolunteerForm()
    return render(request, "master.html", ctx)
