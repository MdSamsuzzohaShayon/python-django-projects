from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer



class UserRegistrationView(APIView):

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            print(user)
            return Response({"message": "Registration success!"}, status=status.HTTP_201_CREATED)
        return Response({"message": serializer.error_messages}, status=status.HTTP_406_NOT_ACCEPTABLE)
    