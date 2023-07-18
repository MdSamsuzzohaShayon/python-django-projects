# https://www.youtube.com/watch?v=xjMP0hspNLE&list=PL-51WBLyFTg1gPEHotYAhNAPsisChkyTc
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# This is kind of documentation for application 
@api_view(['GET'])
def get_routes(request):
    routes = [
        '/api/token/', # retrieve refresh and access token
        '/api/token/refresh/', # Refreshing the token
    ]
    return Response(routes)