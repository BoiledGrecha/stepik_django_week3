from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from accounts.forms import RegisterForm


class MySignupView(CreateView):
    form_class = RegisterForm
    success_url = 'login'
    template_name = 'register.html'

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.get_success_url())


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
