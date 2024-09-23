from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Product
from random import choice
# Create your views here.

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    random_product = choice(products)
    return render(request,'home.html',{"categories":categories,
                                       'products':products,
                                       'random_product':random_product
                                       })
def product(request,category_slug,product_slug):
    try:
        product = Product.objects.get(category__slug = category_slug,slug = product_slug)
    except Exception as Error:
        raise Error
    
    return render(request,'product.html',{
        'product':product
    })
def laptops(request):
    return render(request, 'laptops.html')
def mobiles(request):
    return render(request, 'mobiles.html')