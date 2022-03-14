from django.forms import ModelForm
from products.models import Product

#create a form class
class ProductAddForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('staff',)

        labels = {
            'bp_price':'Buying price per item'
        }