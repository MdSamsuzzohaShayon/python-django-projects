from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product, User
from .serializers import ProductSerializer
import random

# Create your views here.

class ProductViewSet(viewsets.ViewSet):
    def list(self, request): # curl --location --request GET 'http://localhost:8000/api/products'
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return  Response(serializer.data)
    
    def create(self, request): # curl --location --request POST 'http://localhost:8000/api/products' --header 'Content-Type: application/json' --data-raw '{"title": "Title 1", "image": "image 1" }'
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None): # curl --location --request GET 'http://localhost:8000/api/products/1'
        product  = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def update(self, request, pk=None): # curl --location --request PUT 'http://localhost:8000/api/products/1' --header 'Content-Type: application/json' --data-raw '{ "title": "Title 1 update", "image": "image 1" }'
        product  = Product.objects.get(id=pk)
        serializer  = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def destroy(self, request, pk=None): # curl --location --request DELETE 'http://localhost:8000/api/products/1'
        product  = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserAPIView(APIView):
    def get(self, _): # curl --location --request GET 'http://localhost:8000/api/user'
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })
    
