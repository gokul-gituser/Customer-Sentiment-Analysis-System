from django.urls import path, include
from .views import SignUpView
from . import views


app_name = 'customers'
urlpatterns = [
        path("signup/", SignUpView.as_view(), name="signup"),


]