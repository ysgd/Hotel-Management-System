from django.db import models

# Create your models here.
class Menu(models.Model):
  name = models.CharField(max_length=50)
  
class food(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  menu = models.ForeignKey(Menu, on_delete=models.SET_NULL,null=True)
  