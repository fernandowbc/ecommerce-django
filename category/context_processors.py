from .models import Category

#consulta las categorias y las entrega como link
# se regitara en el proyecto en seting.py temolates option
 
def menu_link(request):
    links = Category.objects.all()
    return dict(links=links)