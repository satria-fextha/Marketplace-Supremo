Explicación:

Este archivo de Python define cuatro vistas de Django que se utilizan para administrar las páginas de productos en una aplicación de comercio electrónico de productos agrícolas y ganaderos.

Vista todos_productos:

Esta vista devuelve una lista de todos los productos almacenados en la base de datos. La vista utiliza la función Product.objects.all() para obtener todos los objetos de la clase Product.

Productos Vista_por_categoría:

Esta vista devuelve una lista de productos de una categoría específica. La vista recibe un ID de categoría como parámetro y utiliza la función Product.objects.filter() para obtener los productos que pertenecen a la categoría especificada.

Vista buscar_productos:

Esta vista devuelve una lista de productos que coinciden con una consulta de búsqueda. La vista recibe una cadena de búsqueda como parámetro y utiliza la función Product.objects.filter() para obtener los productos que contienen la cadena de búsqueda en el nombre o la descripción.

Vista filter_products:

Esta vista devuelve una lista de productos que se filtran según varios criterios, como categoría, precio y ubicación. La vista recibe los criterios de filtro como parámetros y utiliza la función Product.objects.filter() para combinar los filtros.

Uso:

Estas vistas se utilizan para mostrar listas de productos en diferentes partes de la aplicación de comercio electrónico. La vista all_products se utiliza para mostrar una lista de todos los productos, la vista products_by_category se utiliza para mostrar una lista de productos de una categoría específica, la vista search_products se utiliza para encontrar productos por nombre o descripción, y la vista filter_products se utiliza para buscar productos por categoría, precio y ubicación.

Ruta:

El archivo de Python se encuentra en la siguiente ruta:

Funcionalidades/Products/views.py
Esta ruta indica que el archivo se encuentra en la carpeta Funcionalidades/Products dentro del proyecto.
from django.shortcuts import render
from .models import Product, Category

def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {'products': products})

def products_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'products_by_category.html', {'category': category, 'products': products})

def search_products(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query) | Product.objects.filter(description__icontains=query)
    return render(request, 'search_products.html', {'query': query, 'products': products})
def filter_products(request):
    category_id = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    location = request.GET.get('location')
    products = Product.objects.all()
    if category_id:
        category = Category.objects.get(id=category_id)
        products = products.filter(category=category)
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    if location:
        products = products.filter(location=location)
    return render(request, 'filter_products.html', {'products': products})
