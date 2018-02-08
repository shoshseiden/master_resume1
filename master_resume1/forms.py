from django import forms

from .states import States

import account.forms


class SignupForm(account.forms.SignupForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    street_address = forms.CharField()
    city = forms.CharField()
    state = forms.CharField(widget=forms.Select(choices=States.STATE_CHOICES))
    zip_code = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]


class SkillForm(forms.Form):
    skill_category = forms.CharField() # i.e. retail, restaurant, etc
    skill_name = forms.CharField()


class WorkForm(forms.Form):
    work_place = forms.CharField()
    work_dates = forms.CharField() # This will change to DateTimeField.
                                    #  Place saver for now.
    work_description = forms.CharField(widget=forms.Textarea)


class EducationForm(forms.Form):
    education_institution = forms.CharField()
    education_degree = forms.CharField()
    education_dates = forms.CharField() # This will change to DateTimeField.
                                        #  Place saver for now.
    education_gpa = forms.CharField() # Might change to IntegerField if needed.
    education_description = forms.CharField(widget=forms.Textarea)


class VolunteerForm(forms.Form):
    volunteer_organization = forms.CharField()
    volunteer_dates = forms.CharField() # This will change to DateTimeField.
                                        #  Place saver for now.
    volunteer_description = forms.CharField(widget=forms.Textarea)
