from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=128, unique=True)
    email = models.EmailField()
    location = models.CharField(max_length=128, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE
    )
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=128, unique=True)
    profile = models.ManyToManyField('Profile', related_name='skills')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=128, unique=True)
    url = models.URLField()
    profile = models.ManyToManyField('Profile', related_name='companies')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Position(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    is_current = models.NullBooleanField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class School(models.Model):
    name = models.CharField(max_length=128, unique=True)
    url = models.URLField()
    profile = models.ManyToManyField('Profile', related_name='schools')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=128)
    url = models.URLField(blank=True, null=True)
    degree = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_current = models.NullBooleanField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    school = models.ForeignKey('School', on_delete=models.CASCADE)
    profile = models.ManyToManyField('Profile', related_name='programs')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=128)
    url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    program = models.ManyToManyField('Program', related_name='courses')
    profile = models.ManyToManyField('Profile', related_name='courses')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=128, unique=True)
    url = models.URLField(blank=True, null=True)
    profile = models.ManyToManyField('Profile', related_name='institutions')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Certification(models.Model):
    name = models.CharField(max_length=128)
    url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    will_expire = models.NullBooleanField()
    valid_from = models.DateField()
    valid_to = models.DateField(blank=True, null=True)
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=128, unique=True)
    url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
