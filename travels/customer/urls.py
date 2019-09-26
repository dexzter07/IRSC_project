from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'customer'

urlpatterns = [
    path('register/signin/login-customer/', auth_views.LoginView.as_view(template_name="customer/login.html"),name='login'),
    path('register/signin/logout-customer/', auth_views.LogoutView.as_view(), name="logout"),
    path('register/customer/', views.SignUp.as_view(), name="customer"),
    path('register/', views.SignUp.as_view(), name="register"),

]
