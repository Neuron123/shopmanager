from django.forms import ModelForm
from products.models import Product
from django.core.exceptions import ValidationError

#create a form class
class ProductAddForm(ModelForm):
    
    class Meta:
        model = Product
        exclude = ('staff','r_quantity')

        labels = {
            'bp_price':'Buying price per item',
            'r_quantity':'Remaining Quantity'
        }