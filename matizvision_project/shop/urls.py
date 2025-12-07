from django.urls import path
from .views import shop_home, product_detail

urlpatterns = [
    path("", shop_home, name="shop_home"),
    path("producto/<slug:slug>/", product_detail, name="product_detail"),
]