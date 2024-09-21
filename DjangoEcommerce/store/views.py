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
def product(request):
    return render(request,'product.html')
def laptops(request):
    return render(request, 'laptops.html')
def mobiles(request):
    return render(request, 'mobiles.html')