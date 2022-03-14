from django.forms import ModelForm
from customers.models import Customer

#create a form class
class CustomerAddForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ('staff',)