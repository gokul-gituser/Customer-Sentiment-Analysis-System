from django.urls import path, include
from .views import SignUpView
from . import views
from django.contrib.auth import views as auth_views



app_name = 'customers'
urlpatterns = [
        path("signup/", SignUpView.as_view(), name="signup"),
        path('login/', auth_views.LoginView.as_view(), name='login'),

        path("logout/", auth_views.LogoutView.as_view(), name="logout"),


]