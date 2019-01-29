from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)#BLANK IS RELATED TO FIELD
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    summary = models.TextField(blank=False, null=False) #NULL IS RELATED TO DATABASE
    featured = models.BooleanField(default=False)
