from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Departments, Employees
from .serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.
@csrf_exempt
def departmentApi(request, id=0):
    
    
    if request.method == 'GET':
        departments = Departments.objects.all()
        # CONVERT INTO JSON USING SERIALIZER CLASS
        department_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(department_serializer.data, safe=False) # IF WE GET ANY ERROR TRYING TO CONVERT JSON THIS SAFE VARIABLE WILL HANDLE THAT
    
    
    elif request.method== 'POST':
        department_data = JSONParser().parse(request)
        # USE SERIALIZER TO CONVERT IT INTO MODEL
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return  JsonResponse("Added successfully")
        return JsonResponse("Failed to add", safe=False)
    
    
    elif request.method == "PUT":
        department_data = JSONParser().parse(request)
        # GET EXISTING RECORD WITH DEPARTMENT ID
        department = Departments.objects.get(DepartmentId = department_data['DepartmentId'])
        # MAPPING IT WITH NEW VALUES USING SERIALIZER
        department_serializer = DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return  JsonResponse("Added successfully")
        return JsonResponse("Failed to add", safe=False)
    
    
    elif request.method == "DELETE":
        # PASSING ID TO DELETE IT FROM URL
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Delete successfully", safe=False)
    