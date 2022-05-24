from django.conf.urls import include
from django.urls import path
from .views import *
app_name = "sales"

urlpatterns = [
    path("sales/", view_Mr_Accounting.as_view(),name="home"),
    #UpdateView
    path('sale_update/<slug:pk>/', UpdateSaleForm.as_view(), name='sale_update'),
    path('sale_delete/<slug:pk>/', DeleteSaleForm.as_view(), name='sale_delete'),
    
    #product buying price
    path('buying_price/<slug:id>/',getBuyingPrice,name="get_bp"),
    path('sales/check_remaining_product/<int:id>/',getRemainingQuantity,name="get_remaining"),

]