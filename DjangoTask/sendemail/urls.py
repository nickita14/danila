from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('success/', success_view, name='success'),
]
