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
from django.urls import path, include
import debug_toolbar
from django.contrib.auth.views import LogoutView

from job_finder import views as job_finder_views
from accounts import views as accounts_views


urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('', job_finder_views.main_view, name="main"),
    path('vacancies/', job_finder_views.all_vacancies_view, name="vacancies"),
    path('vacancies/cat/<str:specialty>', job_finder_views.vacancies_by_specialty_view, name="vacancies_by_categorie"),
    path('companies/<int:company>', job_finder_views.company_view, name="company"),
    path('vacancies/<int:vacancy>', job_finder_views.vacancy_view, name="vacancy"),
    
    path('vacancies/<int:vacancy_id>/send', job_finder_views.send_application_view, name="send_application"),
    path('mycompany/letsstart', job_finder_views.start_create_company_view, name="start_create_company"),
    path('mycompany/create', job_finder_views.create_company_view, name="create_company"),
    path('mycompany', job_finder_views.my_company_view, name="my_company"),
    path('mycompany/vacancies', job_finder_views.my_company_vacancies_view, name="my_company_vacancies"),
    path('mycompany/vacancies/create', job_finder_views.start_create_vacancy_view, name="start_create_vacancy"),
    path('mycompany/vacancies/<int:vacancy_id>', job_finder_views.create_vacancy_view, name="create_vacancy"),
    
    # path('login', accounts_views.login_view, name="login"),
    # path('register', accounts_views.register_view, name="register"),
    # path('logout', accounts_views.logout_view, name="logout"),
    path('login', accounts_views.MyLoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('signup', accounts_views.MySignupView.as_view(), name="register"),
]

handler404 = job_finder_views.error_handler404
handler500 = job_finder_views.error_handler500
