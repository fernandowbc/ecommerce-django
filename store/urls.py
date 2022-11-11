from django.urls import path

from . import views

urlpatterns = [
    path('', views.store, name="store"), #pra redirecionas ala pagona de storage
    path('<slug:category_slug>/', views.store, name="products_by_category"), # url filtro por categoria http://127.0.0.1:8000/store/ropa-de-verano/
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name="product_detail"), # url  detalles del producto http://127.0.0.1:8000/store/Computadoras/cualquiera/

]