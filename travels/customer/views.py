from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView,ListView
from . import forms
from .models import CustomerUser

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "customer/customer.html"