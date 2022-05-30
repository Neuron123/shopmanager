from django.shortcuts import render
from django.views import View
from customers.forms import *
from customers.models import *
#UpdateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
import snoop
from loguru import logger
from django.contrib.auth.decorators import login_required 
# Create your views here.

class view_John_Keen(View):
    @snoop
    # @login_required
    def get(self, request):
        customerAddForm = CustomerAddForm()
        customers = Customer.objects.all()
        return render(request,"customers/index.html",{"customerAddForm":customerAddForm,"customers":customers})

    @snoop
    # @logger.catch
    @login_required
    def post(self,request):
        customer = CustomerAddForm(request.POST)
        customer = customer.save(commit=False)
        customer.staff = request.user
        customer.save()

        #fetch all customers
        customers = Customer.objects.all()
        return render(request,"customers/index.html",{"customers":customers})

#update customer form
class UpdateCustomerForm(UpdateView):
    model = Customer #model
    fields = '__all__' # fields / if you want to select all fields, use "__all__"
    template_name = 'customers/update.html' # templete for updating
    success_url="/dashboard/customers/" # posts list url

#delete customer form
class DeleteCustomerForm(DeleteView):
    model = Customer #model
    template_name = 'customers/delete.html' # templete for deleting
    success_url=reverse_lazy("customers:home")