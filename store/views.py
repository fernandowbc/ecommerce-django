from category.models import Category
from django.shortcuts import get_object_or_404, render

from .models import Product


# Create your views here.
def store(request, category_slug=None):
    #con dicionas consulta d eoroductos por tipo de categoria
    categories = None
    products = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)# devueve las categorias
        products = Product.objects.filter(category=categories, is_available=True)#trae las categorias 
        product_count = products.count()# tra cantidad de productos
        #consultar base de datos y traer los productos activos
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products' : products,
        'product_count' : product_count,
    }
    return render(request, 'store/store.html', context)

# mostras el detalle de losmproductos
def product_detail(request, category_slug, product_slug):
    # ecepcion si los producto no esta cuando se busque(slug) 
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug) #obtien el producto valida el slugm existe buca el slug del productos
    except Exception as e:# si no esta
            raise e

    context = { #si esta lo almacena en diccionario
        'single_product': single_product,
        }     

    return render(request, 'store/product_detail.html', context)
