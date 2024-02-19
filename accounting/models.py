from django.db import models
from frontdesk.models import customer

# Create your models here.
class bill(models.Model):
  customer = models.ForeignKey(customer,on_delete=models.SET_NULL,null=True)
  total_amount = models.IntegerField()
  
class payment(models.Model):
  bill = models.OneToOneField(bill, on_delete=models.SET_NULL,null=True)
  paid_amount = models.IntegerField()