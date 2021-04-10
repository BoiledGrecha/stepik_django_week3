from django.forms import ModelForm, HiddenInput
from job_finder.models import Company, Vacancy
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
    