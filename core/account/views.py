from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic.edit import CreateView
from .forms import UserRegisterForm
from django.views.generic import ListView, TemplateView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
# Create your views here.


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('quiz:test')

    def form_invalid(self, form):
        messages.error(self.request, "Invalid Username or Password")
        return self.render_to_response(self.get_context_data(form=form))


class MySignUpView(CreateView):
    template_name = 'register.html'
    success_url = reverse_lazy('accounts:login')
    form_class = UserRegisterForm
    success_message = "User created successfully"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('quiz:test'))
        return super().dispatch(request, *args, **kwargs)
    
class AccessDeniedView(TemplateView):
    template_name = 'access_denied.html'

class MyPasswordChangeView(PasswordChangeView):
    template_name = 'password-change.html'
    
class MyPasswordChangeDoneView(PasswordChangeDoneView):
    pass
    