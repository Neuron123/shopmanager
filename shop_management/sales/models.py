from django.db import models
from products.models import Product

# Create your models here.
class Sale(models.Model):
    
    unit_type = (('Kg','Kgs'),('Tonnes','Tonnes'),('lts','Litres'))

    staff = models.CharField(max_length=100)
    product_name = models.OneToOneField(Product, on_delete = models.CASCADE)
    # type = models.CharField(max_length=20,choices=unit_type)
    quantity = models.IntegerField()
    bp_price = models.CharField(max_length=20)
    sp_price = models.IntegerField(default = 0)
    profit = models.IntegerField(default = 0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        self.getProduct(self)
        return self.product_name + " - "+ str(self.quantity)
