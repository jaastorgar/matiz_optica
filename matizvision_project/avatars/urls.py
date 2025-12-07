from django.urls import path
from .views import avatar_home

urlpatterns = [
    path('', avatar_home, name='avatar_home'),
]