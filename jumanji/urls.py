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

from job_finder.views import (
                                main_view,
                                all_vacancies_view,
                                vacancies_by_specialty_view,
                                company_view,
                                vacancy_view,
                                error_handler404,
                                error_handler500,
                            )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name="main"),
    path('vacancies/', all_vacancies_view, name="vacancies"),
    path('vacancies/cat/<str:specialty>', vacancies_by_specialty_view, name="vacancies_by_categorie"),
    path('companies/<int:company>', company_view, name="company"),
    path('vacancies/<int:vacancy>', vacancy_view, name="vacancy"),
]

handler404 = error_handler404
handler500 = error_handler500
