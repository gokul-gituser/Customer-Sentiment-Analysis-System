from django.urls import path
from . import views
from django.views.generic.base import TemplateView


app_name = 'website'
urlpatterns = [
    path("", TemplateView.as_view(template_name="website/index.html"), name="index"),

]