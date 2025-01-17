from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('product-name-autocomplete/', views.product_name_autocomplete, name='product-name-autocomplete'),
    path('submit-feedback/', views.submit_feedback, name='submit-feedback'),
]
