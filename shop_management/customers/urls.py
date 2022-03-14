from django.conf.urls import include
from django.urls import path
from .views import *
app_name = "customers"

urlpatterns = [
    path("customers/", view_John_Keen.as_view(),name="home"),
    #UpdateView
    path('customer_update/<slug:pk>/', UpdateCustomerForm.as_view(), name='customer_update'),
    path('customer_delete/<slug:pk>/', DeleteCustomerForm.as_view(), name='customer_delete'),
]