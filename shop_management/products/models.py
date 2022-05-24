from django.db import models

# Create your models here.
class Product(models.Model):
    unit_type = (('Kg','Kgs'),('Tonnes','Tonnes'),('lts','Litres'),('number','Number'))

    staff = models.CharField(max_length=100)
    product_name = models.CharField(max_length=150,unique=True)
    type = models.CharField(max_length=20,choices=unit_type)
    quantity = models.IntegerField()
    r_quantity = models.IntegerField(default="0")


    bp_price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.product_name