from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.front_page,name="front_page"),
    path("signup/",views.signup,name="signup"),
    path("login/",auth_views.LoginView.as_view(template_name="core/login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout")
]