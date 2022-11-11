from django.shortcuts import render
from store.models import Product

def home(request):
    #consulta ala base de taos para traes todos los productos que esta habilitados
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }
    
    return render(request, 'home.html', context)