from django.contrib import admin
from django.urls import path
from .views import ProductViewSet

urlpatterns = [
    path("products", ProductViewSet.as_view({
        'get': 'product_list',
        'post': 'product_create'
    })),
path("products/<str:pk>", ProductViewSet.as_view({
        'get': 'product_single',
        'put': 'product_update',
        'delete': 'product_delete',
    })),
]