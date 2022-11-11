from django.contrib import admin
from .models import Product

# Register your models here.
# calse permite propiedades para lsitas en la admsntarcion de django

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

# registra a la entidad
admin.site.register(Product, ProductAdmin)    