from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='homepage'),
    path('<slug:category_slug>/',views.category,name="category"),
    path('<slug:category_slug>/<slug:product_slug>',views.product, name='product'),
]
