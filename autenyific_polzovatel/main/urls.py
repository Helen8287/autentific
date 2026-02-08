from django.urls import path
from .views import IndexView, ProfileView, RegisterView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', csrf_exempt(LogoutView.as_view(next_page='index')), name='logout'),
]