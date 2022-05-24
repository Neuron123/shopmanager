from django.shortcuts import render
from django.views import View
from products.forms import *
from products.models import *
#UpdateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
import snoop
from loguru import logger 
# Create your views here.

@snoop
#check if product name exists
def check_name(request):
    product = Product.objects.all()
    product_list = []
    for p_name in product:
        product_list.append(p_name.product_name)
    data = {
        "data":product_list
    }
    return JsonResponse(data)

class view_Mr_Warehouse(View):
    @snoop
    def get(self, request):
        productAddForm = ProductAddForm()
        products = Product.objects.all()
        return render(request,"products/index.html",{"productAddForm":productAddForm,"products":products})

    @snoop
    # @logger.catch

    def post(self,request):
        product = ProductAddForm(request.POST)
        product = product.save(commit=False)

        #add current logged in user as staff
        product.staff = request.user

        #add r_quantity for remaining quantity
        product.r_quantity = request.POST.get("quantity")


        #save
        product.save()

        #fetch all customers
        products = Product.objects.all()
        return render(request,"products/index.html",{"products":products})

#update customer form
class UpdateProductForm(UpdateView):
    model = Product #model
    fields = '__all__' # fields / if you want to select all fields, use "__all__"
    template_name = 'products/update.html' # templete for updating
    success_url="/dashboard/products/" # posts list url

#delete customer form
class DeleteProductForm(DeleteView):
    model = Product #model
    template_name = 'products/delete.html' # templete for deleting
    success_url=reverse_lazy("products:home")