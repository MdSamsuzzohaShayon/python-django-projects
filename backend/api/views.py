import json 

from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer

"""
Once you’ve created your data models, Django automatically gives you a database-abstraction API that lets you create, retrieve, update and delete objects. 
Docs: https://docs.djangoproject.com/en/4.2/topics/db/queries/
Model API reference: https://docs.djangoproject.com/en/4.2/ref/models/
"""

# Create your views here.
@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    # instance = Product.objects.all().order_by('?').first()
    # data = {}
    # if instance:
    #     # data = model_to_dict(product_data, fields=['id', 'title', 'price'])
    #     data = ProductSerializer(instance).data

    serializer = ProductSerializer(data=request.data)    
    if serializer.is_valid(raise_exception=True):
        data = serializer.save()
        print(data)
        print(serializer.data)
        return Response(serializer.data)
    # return Response({"message": "Invalid data"}, status=406) # this does not need if we raise exception
