from django.contrib import admin
from .models import Profile, Skill, WorkExperience, Education, VolunteerExperience, CustomResume



class ProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'first_name', 'last_name', 'phone', 'street_address', 'city', 'state', 'zip_code']


class SkillAdmin(admin.ModelAdmin):
    fields = ['skill_category', 'skill_name']


class WorkExperienceAdmin(admin.ModelAdmin):
    fields = ['work_place', 'work_city', 'work_state', 'work_dates', 'work_description']


class EducationAdmin(admin.ModelAdmin):
    fields = ['education_institution', 'education_city', 'education_state', 'education_degree', 'education_dates', 'education_gpa', 'education_description']


class VolunteerExperienceAdmin(admin.ModelAdmin):
    fields = ['volunteer_organization', 'volunteer_city', 'volunteer_state', 'volunteer_dates', 'volunteer_description']


class CustomResumeAdmin(admin.ModelAdmin):
    fieldsets = [('Title and Objective', {'fields': ['custom_resume_title', 'custom_resume_objective']}),
                 ('Contact Information', {'fields': ['profile']}),
                 ('Experience', {'fields': ['skill', 'work', 'education', 'volunteer']}),
                ]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(VolunteerExperience, VolunteerExperienceAdmin)
admin.site.register(CustomResume, CustomResumeAdmin)
