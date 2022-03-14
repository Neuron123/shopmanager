from django.conf.urls import include
from django.urls import path
from .views import *
app_name = "dashboard"

urlpatterns = [
    path("", main,name="home"),
]