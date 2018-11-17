# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from resume.serializers import UserSerializer, GroupSerializer,\
    SkillSerializer, CompanySerializer, PositionSerializer, SchoolSerializer,\
    ProgramSerializer, CourseSerializer, InstitutionSerializer,\
    CertificationSerializer, ProjectSerializer, ProfileSerializer,\
    WebsiteSerializer

from resume.models import Skill, Company, Position, School, Program, Course,\
                          Institution, Certification, Project, Profile, Website


def resume_view(request, username):
    body = ''

    try:
        user = User.objects.all().get(username=username)
    except User.DoesNotExist:
        raise Http404

    user_profile = Profile.objects.all().get(user__id=user.id)

    body += ' {}'.format(user_profile.name)

    return HttpResponse(body, content_type="text/plain")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class WebsiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows websites to be viewed or edited.
    """
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer


class SkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows skills to be viewed or edited.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class PositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows positions to be viewed or edited.
    """
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows schools to be viewed or edited.
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows programss to be viewed or edited.
    """
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class InstitutionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows institutions to be viewed or edited.
    """
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class CertificationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
