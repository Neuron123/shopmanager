from django.db import models
from django.utils import timezone
# from accounts.models import Account
import snoop

# Create your models here.

class Customer(models.Model):
    staff = models.CharField(max_length=100)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.firstname + " - "+ self.lastname

