from django.contrib import admin
from resume.models import Skill, Company, Position, School, Program, Course,\
                          Institution, Certification, Project, Profile
# Register your models here.

resume_models = [Skill, Company, Position, School, Program, Course,
                 Institution, Certification, Project, Profile]

admin.site.register(resume_models)
