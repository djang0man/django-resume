from django.contrib import admin
from resume.models import Interest, Company, Position, School, Program,\
                          Course, Institution, Certification, Project,\
                          Profile, Website
# Register your models here.

resume_models = [Interest, Company, Position, School, Program, Course,
                 Institution, Certification, Project, Profile, Website]

admin.site.register(resume_models)
