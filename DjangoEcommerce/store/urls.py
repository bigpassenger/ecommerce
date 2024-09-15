from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='homepage'),
    path('product',views.product, name='about')
]
