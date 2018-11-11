from django.db import models

# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=128, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=128, unique=True)
    url = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Position(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    is_current = models.NullBooleanField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class School(models.Model):
    name = models.CharField(max_length=128, unique=True)
    url = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=128)
    url = models.URLField(blank=True, null=True)
    degree = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    school = models.ForeignKey('School', on_delete=models.CASCADE)
    is_current = models.NullBooleanField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=128)
    url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    program = models.ForeignKey('Program', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=128, unique=True)
    url = models.URLField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Certification(models.Model):
    name = models.CharField(max_length=128)
    url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    will_expire = models.NullBooleanField()
    valid_from = models.DateField()
    valid_to = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=128, unique=True)
    url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
