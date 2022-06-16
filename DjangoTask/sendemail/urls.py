from django.urls import path
from .views import index, success_view, ContactFormView

urlpatterns = [
    path('', ContactFormView.as_view(), name='home'),
    path('success/', success_view, name='success'),
]
