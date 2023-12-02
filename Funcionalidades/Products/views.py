
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
