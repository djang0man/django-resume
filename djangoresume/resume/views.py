# from django.shortcuts import render

# Create your views here.

import datetime
from dateutil import relativedelta

from django.shortcuts import render

from django.http import JsonResponse, Http404

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from resume.serializers import UserSerializer, GroupSerializer,\
    InterestSerializer, CompanySerializer, PositionSerializer,\
    SchoolSerializer, ProgramSerializer, CourseSerializer,\
    InstitutionSerializer, CertificationSerializer, ProjectSerializer,\
    ProfileSerializer, WebsiteSerializer

from resume.models import Interest, Company, Position, School, Program,\
                          Course, Institution, Certification, Project,\
                          Profile, Website


def resume_get_json(request):
    user = 'stuartdkershaw'
    json_body = get_resume_json(user)
    return JsonResponse(json_body)


def resume_template_view(request):
    user = 'stuartdkershaw'
    json_body = get_resume_json(user)
    return render(request, 'components.html', json_body)


def combine_companies_positions(companies, positions):
    for c in companies:
        c.positions = list()

        for p in positions:
            if p.company_id == c.id:
                c.positions.append(p)

    return companies


def combine_schools_programs_courses(schools, programs, courses):
    for s in schools:
        s.programs = list()

        for p in programs:
            if p.school_id == s.id:
                s.programs.append(p)

            p.courses = list()

            for c in courses:
                if c.program_id == p.id:
                    p.courses.append(c)

    return schools


def combine_institutions_certifications(institutions, certifications):
    for i in institutions:
        i.certifications = list()

        for c in certifications:
            if c.institution_id == i.id:
                i.certifications.append(c)

    return institutions


def get_position_duration(start_date, end_date=None, is_current=False):
    if is_current:
        until_date = datetime.datetime.now()
    elif end_date is not None:
        until_date = datetime.datetime.strptime(str(end_date), '%Y-%m-%d')

    begin_date = datetime.datetime.strptime(str(start_date), '%Y-%m-%d')

    delta = relativedelta.relativedelta(until_date, begin_date)

    duration_string = ''

    if delta.years != 0:
        duration_string += '{} yrs '.format(delta.years)

    if delta.months != 0:
        duration_string += '{} mos'.format(delta.months)

    return duration_string


def get_resume_json(username):
    try:
        user = User.objects.all().get(username=username)
    except User.DoesNotExist:
        raise Http404

    user_profile = Profile.objects.all().get(user__id=user.id)

    user_websites = Website.objects.all().filter(profile__id=user_profile.id)

    user_interests = Interest.objects.all()\
        .filter(profile__id=user_profile.id)\
        .order_by('order_id')

    user_companies = Company.objects.all()\
        .filter(profile__id=user_profile.id)\
        .order_by('order_id')

    user_positions = Position.objects.all()\
        .filter(profile__id=user_profile.id)\
        .order_by('start_date')\
        .reverse()

    user_experience = \
        combine_companies_positions(user_companies, user_positions)

    user_schools = School.objects.all()\
        .filter(profile__id=user_profile.id)\
        .order_by('order_id')

    user_programs = Program.objects.all().filter(profile__id=user_profile.id)

    user_courses = Course.objects.all().filter(profile__id=user_profile.id)

    user_education = \
        combine_schools_programs_courses(
            user_schools, user_programs, user_courses
        )

    user_institutions = Institution.objects.all()\
        .filter(profile__id=user_profile.id)\
        .order_by('order_id')

    user_certifications = \
        Certification.objects.all()\
        .filter(profile__id=user_profile.id)\
        .order_by('valid_from')\
        .reverse()

    user_certificates = \
        combine_institutions_certifications(
            user_institutions, user_certifications
        )

    json_body = {
        'name': user_profile.name,
        'email': user_profile.email,
        'location': user_profile.location,
        'about': user_profile.about,
        'websites': [
            {
                'name': w.name,
                'url': w.url
            } for w in user_websites
        ],
        'interests': [
            s.name for s in user_interests
        ],
        'experience': {
            'companies': [
                {
                    'name': c.name,
                    'location': c.location,
                    'url': c.url,
                    'positions': [
                        {
                            'title': p.title,
                            'start_date': p.start_date,
                            'end_date': p.end_date,
                            'is_current': p.is_current,
                            'duration': get_position_duration(p.start_date, p.end_date, p.is_current),
                            'description': p.description
                        } for p in c.positions
                    ]
                } for c in user_experience
            ]
        },
        'education': {
            'schools': [
                {
                    'name': s.name,
                    'location': s.location,
                    'url': s.url,
                    'programs': [
                        {
                            'name': p.name,
                            'url': p.url,
                            'degree': p.degree,
                            'start_date': p.start_date,
                            'end_date': p.end_date,
                            'is_current': p.is_current,
                            'description': p.description,
                            'courses': [
                                {
                                    'name': c.name,
                                    'url': c.url,
                                    'description': c.description
                                } for c in p.courses
                            ]
                        } for p in s.programs
                    ]
                } for s in user_education
            ]
        },
        'certifications': {
            'institutions': [
                {
                    'name': i.name,
                    'url': i.url,
                    'certificates': [
                        {
                            'name': c.name,
                            'url': c.url,
                            'expires': c.will_expire,
                            'valid_from': c.valid_from,
                            'valid_until': c.valid_to,
                            'description': c.description
                        } for c in i.certifications
                    ]
                } for i in user_certificates
            ]
        }
    }

    return json_body


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
    queryset = Group.objects.get_queryset().order_by('id')
    serializer_class = GroupSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Profile.objects.get_queryset().order_by('id')
    serializer_class = ProfileSerializer


class WebsiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows websites to be viewed or edited.
    """
    queryset = Website.objects.get_queryset().order_by('id')
    serializer_class = WebsiteSerializer


class InterestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows skills to be viewed or edited.
    """
    queryset = Interest.objects.get_queryset().order_by('id')
    serializer_class = InterestSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Company.objects.get_queryset().order_by('id')
    serializer_class = CompanySerializer


class PositionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows positions to be viewed or edited.
    """
    queryset = Position.objects.get_queryset().order_by('id')
    serializer_class = PositionSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows schools to be viewed or edited.
    """
    queryset = School.objects.get_queryset().order_by('id')
    serializer_class = SchoolSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows programss to be viewed or edited.
    """
    queryset = Program.objects.get_queryset().order_by('id')
    serializer_class = ProgramSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Course.objects.get_queryset().order_by('id')
    serializer_class = CourseSerializer


class InstitutionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows institutions to be viewed or edited.
    """
    queryset = Institution.objects.get_queryset().order_by('id')
    serializer_class = InstitutionSerializer


class CertificationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Certification.objects.get_queryset().order_by('id')
    serializer_class = CertificationSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = Project.objects.get_queryset().order_by('id')
    serializer_class = ProjectSerializer
