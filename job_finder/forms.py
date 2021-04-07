from django.forms import ModelForm, HiddenInput
from job_finder.models import Company

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'owner':HiddenInput(),
            'logo':HiddenInput(),
        }