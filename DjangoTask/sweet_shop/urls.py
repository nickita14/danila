from django.conf.urls.static import static
from django.urls import path

import settings
from .views import (
    ShopMain,
    ShowProduct,
    ProductCategory,
    page_not_found,
    SearchPage,
)

urlpatterns = [
    path('shop/', ShopMain.as_view(), name='shop'),
    path('product/<slug:product_slug>', ShowProduct.as_view(), name='product'),
    path('category/<slug:category_slug>', ProductCategory.as_view(), name='category'),
    path('search/', SearchPage.as_view(), name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found
