from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product

# Field-level validation
# def validate_title(value):
#     # qs = Product.objects.filter(title__exact=value)
#     qs = Product.objects.filter(title__iexact=value) # Case in sensative
#     if qs.exists():
#         raise serializers.ValidationError(f"There is already a product registered with name of {value}!")
#     return value


def validate_titile_no_hello(value):
    if 'hello' in value.lower():
        raise serializers.ValidationError(f"Hello is not allowed!")
    return value



unique_product_title = UniqueValidator(queryset=Product.objects.all())