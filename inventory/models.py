from django.db import models

# Create your models here.
class Category(models.Model):  
    name = models.CharField(max_length=100)  
    description = models.TextField(blank=True)  

    def __str__(self):  
        return self.name  

class Product(models.Model):  
    name = models.CharField(max_length=200)  
    description = models.TextField(blank=True)  
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    quantity = models.IntegerField(default=0)  
    sku = models.CharField(max_length=50, unique=True)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):  
        return self.name  