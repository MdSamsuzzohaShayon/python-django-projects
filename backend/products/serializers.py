from . import validators

from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product

"""
write your own custom validators.
https://www.django-rest-framework.org/api-guide/validators/#field-level-validation
https://www.django-rest-framework.org/api-guide/fields/
"""


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    update_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field="pk")

    # Method-1: validate in external module
    # title = serializers.CharField(validators=[validators.validate_title])
    title = serializers.CharField(validators=[validators.validate_titile_no_hello, validators.unique_product_title])
    # name = serializers.CharField(source="title")

    class Meta:
        model = Product
        fields = [
            "url",
            "update_url",
            "id",
            "pk",
            "title",
            # "name",
            "content",
            "price",
            "sale_price",
            "my_discount",
        ]

    # Method-2: validate in internal module
    # Field-level validation
    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     # qs = Product.objects.filter(title__exact=value)
    #     qs = Product.objects.filter(title__iexact=value) # Case in sensative
    #     if qs.exists():
    #         raise serializers.ValidationError(f"There is already a product registered with name of {value}!")
    #     return value

    # Override default method for creating email in Product model -> We can also do this from perform_create method from views.py
    # def create(self, validated_data):
    #     # email = validated_data.pop("email")
    #     # return Product.objects.create(**validated_data)
    #     obj =  super().create(validated_data) # Another option to return validated data
    #     # print(email, obj)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title") + "U"
    #     return instance

    def get_update_url(self, obj):
        # return f'/api/products/{obj.pk}/' # Wrong way

        # Right way
        request = self.context.get("request")
        if request is None:
            return None
        # update-product is the name of url from urls.py
        return reverse("update-product", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        # Prevent serielizer error of getting no value of get_discount
        if not hasattr(
            obj, "id"
        ):  # when we create, read, update from database we get the id.
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
