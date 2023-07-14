from rest_framework import generics, mixins
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer
from api.mixins import StaffEditorPermissionMixin

# Create your views here.
"""
Used for read-only endpoints to represent a single model instance. -> https://www.django-rest-framework.org/api-guide/generic-views/#retrieveapiview
Example: https://www.django-rest-framework.org/api-guide/generic-views/#examples
Function Based Views: https://www.django-rest-framework.org/api-guide/views/#function-based-views
Authentication: https://www.django-rest-framework.org/api-guide/authentication/
Permissions(Protecting routes): https://www.django-rest-framework.org/api-guide/permissions/
DjangoModelPermissions: https://www.django-rest-framework.org/api-guide/permissions/#djangomodelpermissions
Custom permissions: https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions
"""
class ProductDetailAPIView(StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

class ProductListCreateAPIView( StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # add additional content
    def perform_create(self, serializer):
        # email = serializer.validated_data.pop('email')
        # print(email)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None or content == '':
            content = title 
        serializer.save(content=content)

class ProductCreateAPIView(StaffEditorPermissionMixin, generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # add additional content
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None or content == '':
            content = title 
        serializer.save(content=content)

class ProductListAPIView(StaffEditorPermissionMixin, generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

class ProductDestroyAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_distroy(self, instance):
        super().perform_distroy(instance)
    
class ProductMixinView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None or content == '':
            content = title 
        serializer.save(content=content)

# @api_view(["GET", "POST"])
# def product_alt_view(request, pk=None, *args, **kwargs):

#     if request.method == "GET":
#         if pk is None:
#             queryset = Product.objects.all()
#             data = ProductSerializer(queryset, many=True).data
#             return Response(data)
        
#         # queryset = Product.objects.filter(pk=pk)
#         # if not queryset.exists:
#         #     raise Http404
#         obj = get_object_or_404(Product, pk=pk)
#         data = ProductSerializer(obj, many=False).data
#         return Response(data)
    
#     if request.method == "POST":
#         serializer = ProductSerializer(data=request.data)    
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content')
#             if content is None or content == '':
#                 content = title 
#             serializer.save(content=content)
#             return Response(serializer.data) 
#         return Response({"message": "Invalid data"})
