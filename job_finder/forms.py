from django.forms import ModelForm, HiddenInput
from job_finder.models import Company, Vacancy, Application
from datetime import date


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'owner':HiddenInput(),
            'logo':HiddenInput(),
        }

class VacancyForm(ModelForm):
    
    class Meta:
        model = Vacancy
        fields = '__all__'
        widgets = {
            'id':HiddenInput(),
            'company':HiddenInput(),
            'published_at':HiddenInput(),
        }

class ApplicationForm(ModelForm):
    
    class Meta:
        model = Application
        fields = '__all__'
        widgets = {
            'vacancy':HiddenInput(),
            'user':HiddenInput(),
        }
    