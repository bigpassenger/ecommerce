from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name
class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='company',blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'company'
        verbose_name_plural = 'companies'
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='product',blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default='True')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name