from django.urls import path
from . import views

app_name = 'api'

#URL patterns for the API endpoints
urlpatterns = [
    #Endpoint for product name autocomplete
    path('product-name-autocomplete/', views.product_name_autocomplete, name='product-name-autocomplete'),
    #Endpoint for submitting customer feedback
    path('submit-feedback/', views.submit_feedback, name='submit-feedback'),
]
