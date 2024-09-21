from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Product
# Create your views here.

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request,'home.html',{"categories":categories,
                                       'products':products})
def product(request):
    return render(request,'product.html')
def laptops(request):
    return render(request, 'laptops.html')
def mobiles(request):
    return render(request, 'mobiles.html')