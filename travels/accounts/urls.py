from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/signin/login-hotel/', auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    path('register/signin/logout-hotel/', auth_views.LogoutView.as_view(), name="logout"),
    path('register/hotel/',views.SignUp.as_view(), name="hotel"),
    path('register',views.Register.as_view(),name="register"),
    path('register/signin/', views.Login.as_view(),name='page'),

]
