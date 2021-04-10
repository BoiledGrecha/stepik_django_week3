from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from random import sample
from datetime import date
from job_finder.models import Vacancy, Specialty, Company
from job_finder.forms import CompanyForm, VacancyForm



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
    try:
        context["vacancy"] = Vacancy.objects.get(id=vacancy)
    except ObjectDoesNotExist:
        raise Http404
    return render(request, "week3/vacancy.html", context)

##################################################
def send_application_view(request):
    context = {}
    return render(request, "week4/sent", context)


def start_create_company_view(request):
    context = {}
    return render(request, "week3/company-create.html", context)


def create_company_view(request):
    pass

@login_required
def my_company_view(request):
    try:
        company_form = CompanyForm(instance=Company.objects.get(owner_id=request.user.id))
        return render(request, "week3/company-edit.html", {"form": company_form})
    except:
        return render(request, "week3/company-create.html")

@login_required
def my_company_vacancies_view(request):
    context = {}
    context["vacancies"] = Vacancy.objects.filter(company__owner_id=request.user.id)
    return render(request, "week4/vacancy-list.html", context)

@login_required
def create_vacancy_view(request):
    context = {}
    if request.method == "POST":
        if not request.POST["published_at"]:
            request.POST._mutable = True
            request.POST['published_at'] = date.today().strftime("%Y-%m-%d")
        try:
            vacancy_form = VacancyForm(request.POST, instance=Vacancy.objects.get(id=request.POST["vacancy_id"]))
        except:
            vacancy_form = VacancyForm(request.POST)
        
        if vacancy_form.is_valid():
            vacancy_form.save()
            return redirect(my_company_vacancies_view)
            
    vacancy_form = VacancyForm(initial={'company':Company.objects.get(owner_id=request.user.id)})
    return render(request, "week4/vacancy-edit.html", {"form":vacancy_form})


##########\/\/\/\/\/\/\/\/\/\/\/##################
@login_required
def edit_vacancy_view(request, vacancy_id):
    context = {}
    vacancy_form = VacancyForm(instance=Vacancy.objects.get(id=vacancy_id))
    return render(request, "week4/vacancy-edit.html", {"form":vacancy_form, "vacancy_id":vacancy_id})


@login_required
def create_company_view(request):
    if request.method == "POST":
        try:
            company_form = CompanyForm(request.POST, instance=Company.objects.get(owner=User.objects.get(id=request.user.id)))
        except:
            company_form = CompanyForm(request.POST)
        
        if company_form.is_valid():
            company_form.save()
        # add if not valid

    try:
        company = Company.objects.get(owner_id=request.user.id)
        return redirect(my_company_view)
    except:
        company_form = CompanyForm(initial={'owner':User.objects.get(id=request.user.id)})
        return render(request, "week3/company-edit.html", {"form":company_form})

@login_required
def send_application_view(request):
    pass


def error_handler500(request, *args, **kwargs):
    return HttpResponse('Something is going wrong, please contact us +7 800 555 35 35 ', status=500)


def error_handler404(request, *args, **kwargs):
    return HttpResponse('You are trying to access unknown page', status=404)
