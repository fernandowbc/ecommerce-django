from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
# matenimiento de los productos,

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    descriptions = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #si elimana la categoria elimana los prodictioa rela cionado alla categoria
    create_date = models.DateTimeField(auto_now_add=True)# fecah de cracion y se auto genera
    modified_date = models.DateTimeField(auto_now=True) # fecha  modificacion

    #url dinamicas para los productos
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])# product_detail viene desde urls.py, se implementa el el home http://127.0.0.1:8000/store/accesorios-tech/headphones/


# lo que quiero listas y como
    def __str__(self):
        return self.product_name
       



