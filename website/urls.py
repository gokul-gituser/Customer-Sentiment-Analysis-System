from django.urls import path
from . import views
from django.views.generic.base import TemplateView


app_name = 'website'
urlpatterns = [
   path("", views.index, name="index"),
]