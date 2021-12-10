from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Departments, Employees
from .serializers import DepartmentSerializer, EmployeeSerializer
from django.core.files.storage import default_storage

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
            return  JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    
    
    elif request.method == "PUT":
        department_data = JSONParser().parse(request)
        # GET EXISTING RECORD WITH DEPARTMENT ID
        department = Departments.objects.get(DepartmentId = department_data['DepartmentId'])
        # MAPPING IT WITH NEW VALUES USING SERIALIZER
        department_serializer = DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return  JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    
    
    elif request.method == "DELETE":
        # PASSING ID TO DELETE IT FROM URL
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Delete successfully", safe=False)


@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employee_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
    
    
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    
    
    elif request.method == "PUT":
        
        employee_data = JSONParser().parse(request)
        # print("ID - ", employee_data['EmployeeId'])
        employee = Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        # employee = Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        # print(employee)
        # MAPPING IT WITH NEW VALUES USING SERIALIZER
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        # print("Check validity - ", employee_serializer.is_valid())
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    
    
    elif request.method == "DELETE":
        # PASSING ID TO DELETE IT FROM URL
        employee = Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Delete successfully", safe=False)
    
    
@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    print("FIle - ", file)
    file_name= default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)