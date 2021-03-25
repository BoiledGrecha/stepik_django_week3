from django.db import models


class Specialty(models.Model):
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    picture = models.URLField(max_length=500, default='https://place-hold.it/100x60')

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    logo = models.URLField(max_length=500, default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()

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
    published_at = models.DateField()

    def __str__(self):
        return self.name
