from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse, Http404
from random import sample
from job_finder.models import Vacancy, Specialty, Company


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


def error_handler500(request, *args, **kwargs):
    return HttpResponse('Something is going wrong, please contact us +7 800 555 35 35 ', status=500)


def error_handler404(request, *args, **kwargs):
    return HttpResponse('You are trying to access unknown page', status=404)
