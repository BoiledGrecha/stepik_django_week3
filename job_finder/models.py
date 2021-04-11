from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Specialty(models.Model):
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    picture = models.URLField(max_length=500, default='https://place-hold.it/100x60')

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    logo = models.URLField(max_length=500, default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.CharField(max_length=200)
    owner = models.OneToOneField(User,  on_delete=models.CASCADE, related_name='company', null=True)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField(default=date.today().strftime("%Y-%m-%d"))

    def __str__(self):
        return self.title


class Application(models.Model):
    written_name = models.CharField(max_length=50)
    written_phone = models.CharField(max_length=100)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')

    def __str__(self):
        return self.written_name
