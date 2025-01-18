from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomerCreationForm

#New user registration
class SignUpView(CreateView):
    #form to be used for the customer registration process
    form_class = CustomerCreationForm
    # redirects the user to the login page after successful registration
    success_url = reverse_lazy("login")
    #template to render the sign-up form
    template_name = "registration/signup.html"