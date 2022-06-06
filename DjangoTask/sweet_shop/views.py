from django.http import HttpResponse

from sweet_shop.models import *


def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
