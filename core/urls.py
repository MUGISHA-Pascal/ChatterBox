from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.front_page,name="front_page"),
]