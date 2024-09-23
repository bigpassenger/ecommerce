from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='homepage'),
    path('<slug:category_slug>/<slug:product_slug>',views.product, name='product'),
    path('laptops',views.laptops,name="laptops"),
    path('mobiles',views.mobiles,name='mobiles')
]
