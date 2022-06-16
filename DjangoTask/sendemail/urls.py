from django.urls import path
from .views import success_view, ContactFormView

urlpatterns = [
    path('', ContactFormView.as_view(), name='home'),
    path('success/', success_view, name='success'),
]
