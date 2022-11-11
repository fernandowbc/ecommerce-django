from django.contrib import admin
from .models import Category

# Register your models here.
# para que el slug se autogenere

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)} # se lelna con el nmbre de la taregoria
    list_display = ('category_name', 'slug') # columnas o campos amostarr ene le admin
    

admin.site.register(Category, CategoryAdmin)
