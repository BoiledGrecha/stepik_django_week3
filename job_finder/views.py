from django.shortcuts import render
from random import sample
from job_finder.models import Vacancy, Specialty, Company


def main_view(request):
    context = {}
    all_specialties = Specialty.objects.all()
    context["specialties"] = sample(list(all_specialties), len(all_specialties))
    
    return render(request, "week3/index.html", context)


def all_vacancies_view(request):
    context = {}
    return render(request, "week3/vacancies.html", context)


def vacancies_by_specialty_view(request, specialty):
    context = {}
    return render(request, "week3/vacancies.html", context)


def company_view(request, company):
    context = {}
    return render(request, "week3/company.html", context)


def vacancy_view(request, company):
    context = {}
    return render(request, "week3/vacancy.html", context)

# # переписать хендлеры отталкиваясь от ревью
# def error_handler500(request, *args, **kwargs):
#     return HttpResponse('Something is going wrong, please contact us +7 800 555 35 35 ', status=500)


# def error_handler404(request, *args, **kwargs):
#     return HttpResponse('You are trying to access unknown page', status=404)