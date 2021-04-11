from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from random import sample
from job_finder.models import Vacancy, Specialty, Company, Application
from job_finder.forms import CompanyForm, VacancyForm, ApplicationForm


def main_view(request):
    context = {}
    all_specialties = Specialty.objects.all()
    context["specialties"] = sample(list(all_specialties), len(all_specialties))
    all_companies = Company.objects.all()
    context["companies"] = sample(list(all_companies), min(len(all_companies), 8))
    return render(request, "week3/index.html", context)


def all_vacancies_view(request):
    context = {}
    context["specialties"] = Specialty.objects.all()
    return render(request, "week3/vacancies.html", context)


def vacancies_by_specialty_view(request, specialty):
    context = {}
    try:
        context["specialties"] = Specialty.objects.filter(id=specialty)
        if not context["specialties"]:
            raise ObjectDoesNotExist
    except ObjectDoesNotExist:
        raise Http404
    return render(request, "week3/vacancies.html", context)


def company_view(request, company):
    context = {}
    try:
        context["company"] = Company.objects.get(id=company)
    except ObjectDoesNotExist:
        raise Http404
    return render(request, "week3/company.html", context)


def vacancy_view(request, vacancy):
    context = {}
    context["vacancy"] = Vacancy.objects.get(id=vacancy)
    application_form = ApplicationForm(initial={'user': request.user, 'vacancy': Vacancy.objects.get(id=vacancy)})
    context["form"] = application_form
    return render(request, "week3/vacancy.html", context)


def start_create_company_view(request):
    context = {}
    return render(request, "week3/company-create.html", context)


@login_required
def my_company_view(request):
    try:
        company_form = CompanyForm(instance=Company.objects.get(owner_id=request.user.id))
        return render(request, "week3/company-edit.html", {"form": company_form})
    except ObjectDoesNotExist:
        return render(request, "week3/company-create.html")


@login_required
def my_company_vacancies_view(request):
    context = {}
    context["vacancies"] = Vacancy.objects.filter(company__owner_id=request.user.id)
    return render(request, "week4/vacancy-list.html", context)


@login_required
def create_vacancy_view(request):
    if request.method == "POST":
        try:
            vacancy_form = VacancyForm(request.POST, instance=Vacancy.objects.get(id=request.POST["vacancy_id"]))
        except (ObjectDoesNotExist, MultiValueDictKeyError):
            vacancy_form = VacancyForm(request.POST)
        if vacancy_form.is_valid():
            vacancy_form.save()
            return redirect(my_company_vacancies_view)
    vacancy_form = VacancyForm(initial={'company': Company.objects.get(owner_id=request.user.id)})
    return render(request, "week4/vacancy-edit.html", {"form": vacancy_form})


@login_required
def edit_vacancy_view(request, vacancy_id):
    vacancy_form = VacancyForm(instance=Vacancy.objects.get(id=vacancy_id))
    applications = Application.objects.filter(vacancy__id=vacancy_id)
    return render(request, "week4/vacancy-edit.html", {"form": vacancy_form,
                                                       "vacancy_id": vacancy_id,
                                                       "applications": applications})


@login_required
def create_company_view(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        company = Company.objects.filter(owner=user)
        company_form = (CompanyForm(request.POST) if not company
                        else CompanyForm(request.POST, instance=company[0]))
        if company_form.is_valid():
            company_form.save()
            return redirect(my_company_view)
    company_form = CompanyForm(initial={'owner': User.objects.get(id=request.user.id)})
    return render(request, "week3/company-edit.html", {"form": company_form})


@login_required
def send_application_view(request, vacancy_id):
    if request.POST:
        application_form = ApplicationForm(request.POST)
        if application_form.is_valid():
            application_form.save()
    return render(request, "week4/sent.html", {"vacancy_id": vacancy_id})


def error_handler500(request, *args, **kwargs):
    return HttpResponse('Something is going wrong, please contact us +7 800 555 35 35 ', status=500)


def error_handler404(request, *args, **kwargs):
    return HttpResponse('You are trying to access unknown page', status=404)
