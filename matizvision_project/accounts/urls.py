from django.urls import path
from .views import register_view, LoginForm, logout_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', LoginForm, name='login'),
    path("logout/", logout_view, name="logout"),
]