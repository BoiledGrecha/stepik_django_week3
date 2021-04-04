from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView



class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'register.html'
    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.get_success_url())


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'


def login_view(request):
    return render(request, "week4/login.html")


def register_view(request):
    pass


def logout_view(request):
    pass
