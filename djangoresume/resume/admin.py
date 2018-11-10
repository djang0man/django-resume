from django.contrib import admin
from resume.models import Skill, Company, Position
# Register your models here.

resume_models = [Skill, Company, Position]

admin.site.register(resume_models)
