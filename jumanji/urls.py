"""jumanji URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from job_finder.views import main_view, all_vacancies_view, vacancies_by_speciality_view, company_view, vacancy_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('vacancies/', all_vacancies_view),
    path('vacancies/cat/<str:speciality>', vacancies_by_speciality_view),
    path('companies/<int:company>', company_view),
    path('vacancies/<int:vacancy>', vacancy_view),
]

# handler404 = error_handler404
# handler500 = error_handler500