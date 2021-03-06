from django.db import models
from django.contrib.auth.models import User


# Master Resume Models
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    street_address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=15)
    zip_code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "%s" % self.user


class Skill(models.Model):
    skill_category = models.CharField(max_length=50) # i.e. retail, restaurant, etc
    skill_name = models.CharField(max_length=50)

    def __str__(self):
        return self.skill_name


class WorkExperience(models.Model):
    work_place = models.CharField(max_length=150)
    work_city = models.CharField(max_length=50)
    work_state = models.CharField(max_length=15)
    work_dates = models.CharField(max_length=25) # This will change to DateTimeField.
                                                #  Place saver for now.
    work_description = models.TextField(blank=True)

    def __str__(self):
        return self.work_place


class Education(models.Model):
    education_institution = models.CharField(max_length=150)
    education_city = models.CharField(max_length=50)
    education_state = models.CharField(max_length=15)
    education_degree = models.CharField(max_length=100)
    education_dates = models.CharField(max_length=25) # This will change to DateTimeField.
                                                     #  Place saver for now.
    education_gpa = models.CharField(max_length=4) # Might change to IntegerField if needed.
    education_description = models.TextField(blank=True)

    def __str__(self):
        return self.education_institution


class VolunteerExperience(models.Model):
    volunteer_organization = models.CharField(max_length=150)
    volunteer_city = models.CharField(max_length=50)
    volunteer_state = models.CharField(max_length=15)
    volunteer_dates = models.CharField(max_length=25) # This will change to DateTimeField.
                                                     #  Place saver for now.
    volunteer_description = models.TextField(blank=True)

    def __str__(self):
        return self.volunteer_organization

# Custom Resume Models
class CustomResume(models.Model):
    profile = models.ForeignKey(Profile)
    skill = models.ForeignKey(Skill)
    work = models.ForeignKey(WorkExperience)
    education = models.ForeignKey(Education)
    volunteer = models.ForeignKey(VolunteerExperience)

    custom_resume_title = models.CharField(max_length=150)
    custom_resume_objective = models.TextField(blank=True)

    def __str__(self):
        return self.custom_resume_title
