from django.urls import path
from .views import *

urlpatterns = [
    path('shop/', shop, name='shop'),
    path('product/<slug:product_slug>', show_product, name='product'),
    path('category/<slug:category_slug>', show_category, name='category'),
]
