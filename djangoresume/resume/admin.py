from django.contrib import admin
from resume.models import Skill, Company, Position, School, Program, Course,\
                          Institution, Certification, Project, Profile, Website
# Register your models here.

resume_models = [Skill, Company, Position, School, Program, Course,
                 Institution, Certification, Project, Profile, Website]

admin.site.register(resume_models)
