from django.forms import ModelForm
from sales.models import Sale
from products.models import Product

#create a form class
class SaleAddForm(ModelForm):
    class Meta:
        model = Sale
        exclude = ('staff',)