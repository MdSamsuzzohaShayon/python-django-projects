from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# Create your views here.


class ProductViewSet(viewsets.ViewSet):

    def product_list(self, request):  # /api/products
        products = Product.objects.all()
        serielizer = ProductSerializer(products, many= True)
        return Response(serielizer.data)

    def product_create(self, request): # /api/products
        serielizer = ProductSerializer(data=request.data)
        serielizer.is_valid(raise_exception=True)
        serielizer.save()
        return Response(serielizer.data, status=status.HTTP_201_CREATED)

    def product_single(self, request, pk=None): # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serielizer = ProductSerializer(product)
        return Response(serielizer.data)

    def product_update(self, request, pk=None): # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serielizer  = ProductSerializer(instance = product, data = request.data)
        serielizer.is_valid(raise_exception=True)
        serielizer.save()
        return Response(serielizer.data, status=status.HTTP_202_ACCEPTED)


    def product_delete(self, request, pk=None): # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

