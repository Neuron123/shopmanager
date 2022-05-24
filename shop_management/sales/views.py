from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from django.views import View
from sales.forms import *
from sales.models import *
from products.models import *

#UpdateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
import snoop
from loguru import logger 
# Create your views here.


class view_Mr_Accounting(View):
    @snoop
    def get(self, request):
        saleAddForm = SaleAddForm()
        sales = Sale.objects.all()
        return render(request,"sales/index.html",{"saleAddForm":saleAddForm,"sales":sales})

    @snoop
    # @logger.catch
    def post(self,request):
        sale = SaleAddForm(request.POST)
        sale = sale.save(commit=False)
        sale.staff = request.user

        # save
        sale.save()
        
        p_qty = request.POST.get("quantity")
        pname = request.POST.get("product_name")
        product = Product.objects.all()
        
        for p in product.values():
            if p["id"] == int(pname):
                print(p["r_quantity"])
                r_quantity = int(p["r_quantity"]) - int(p_qty) 
                Product.objects.filter(id = p["id"]).update(r_quantity = r_quantity)
                

        #fetch all customers
        sales = Sale.objects.all()
        return render(request,"sales/index.html",{"sales":sales})

#update customer form
class UpdateSaleForm(UpdateView):
    model = Sale #model
    fields = '__all__' # fields / if you want to select all fields, use "__all__"
    template_name = 'sales/update.html' # templete for updating
    success_url="/dashboard/sales/" # posts list url

#delete customer form
class DeleteSaleForm(DeleteView):
    model = Sale #model
    template_name = 'sales/delete.html' # templete for deleting
    success_url=reverse_lazy("sales:home")

# @logger.catch
def getBuyingPrice(request,id):
    product = Product.objects.filter(id=id)
    product_bp = product.values()[0]['bp_price']
    # return HttpResponse(status=200)
    data = {
        "data":product_bp,
    }
    return JsonResponse(data)

#check how much is there
def getRemainingQuantity(request,id):
    product = Product.objects.filter(id=id)
    product_remaining = product.values()[0]['r_quantity']
    product_remaining = {
        "data":product_remaining,
    }
    return JsonResponse(product_remaining)