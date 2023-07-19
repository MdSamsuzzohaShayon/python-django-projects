from rest_framework import serializers
from accounts.models import User 


class UserRegistrationSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    
    class Meta:
        model = User 
        fields = "__all__"
        # fields = ["email", "name", "password", "password2", "tc"]
        extra_kwargs = {
            "password2": {"write_only": True}
        }

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError('Password did not match!')
        return attrs
    

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = User 
        fields = ["email", "password"]