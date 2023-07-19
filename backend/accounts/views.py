from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import authenticate



class UserRegistrationView(APIView):

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            print(user)
            return Response({"message": "Registration success!"}, status=status.HTTP_201_CREATED)
        return Response({"message": serializer.error_messages}, status=status.HTTP_406_NOT_ACCEPTABLE)
    

class UserLoginView(APIView):

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if request.data and serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(request=request, email=email, password=password)
            print(email, password, user)
            if user is not None:
                return Response({"message": "Login success!"}, status=status.HTTP_200_OK)
        return Response({"message": "Login failure!"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    