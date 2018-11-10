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

    def __str__(self):
        return self.name


class Position(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    is_current = models.NullBooleanField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
