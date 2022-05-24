from django.conf.urls import include
from django.urls import path
from .views import *
app_name = "products"

urlpatterns = [
    path("products/", view_Mr_Warehouse.as_view(),name="home"),
    path("check_product/",check_name,name="check_name"),
    #UpdateView
    path('product_update/<slug:pk>/', UpdateProductForm.as_view(), name='product_update'),
    path('product_delete/<slug:pk>/', DeleteProductForm.as_view(), name='product_delete'),
]