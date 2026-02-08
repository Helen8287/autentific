from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import redirect

class IndexView(TemplateView):
    template_name = 'main/index.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'main/profile.html'
    login_url = reverse_lazy('login')

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

def logout_view(request):
    logout(request)
    return redirect('login')  # 'login' — это имя URL для страницы входа




