from django.conf.urls import include
from django.urls import path
from accounts.views import *

app_name='accounts'

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('signup/', signup, name='signup'),
]