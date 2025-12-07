from django.urls import path
from .views import shop_home

urlpatterns = [
    path('', shop_home, name='shop_home'),
]