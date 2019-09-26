from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView,ListView
from . import forms
from .models import HotelUser

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/hotel.html"

class Register(TemplateView):
    template_name = "hotels/register.html"

class Login(TemplateView):
    template_name = "accounts/signin.html"
