from django.forms import ModelForm, HiddenInput
from job_finder.models import Company, Vacancy, Application


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'location', 'logo', 'description', 'employee_count', 'owner']
        widgets = {
            'owner': HiddenInput(),
            'logo': HiddenInput(),
        }


class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'specialty', 'company', 'skills', 'description', 'salary_min', 'salary_max', 'published_at']
        widgets = {
            'id': HiddenInput(),
            'company': HiddenInput(),
            'published_at': HiddenInput(),
        }


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['written_name', 'written_phone', 'written_cover_letter', 'vacancy', 'user']
        widgets = {
            'vacancy': HiddenInput(),
            'user': HiddenInput(),
        }
