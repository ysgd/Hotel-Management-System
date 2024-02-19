from django.db import models
from management.models import Room

# Create your models here.
class customer(models.Model):
  name = models.CharField(max_length=200)
  address = models.TextField()
  email = models.EmailField()
  contact = models.IntegerField()
  
class customerRoom(models.Model):
  customer = models.ForeignKey(customer, on_delete=models.SET_NULL,null=True)
  room = models.ForeignKey(Room, on_delete=models.SET_NULL,null=True)
  