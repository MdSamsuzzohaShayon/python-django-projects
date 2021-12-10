# SERIALIZERS BASICALLY HELP TO CONVERT COMPLEX TYPES OR MODEL INSTANCES INTO NATIVE PYTHON DATA TYPE THAT CAN THEN BE EASILY INTO JSON OR XML
# IT'S ALSO HELP IN DESERIALIZATION
# CONVERTING THE PAST DATA BACK TO COMPLEX TYPES

from rest_framework import serializers
from .models import Departments, Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields=('DepartmentId', 'DepartmentName', )
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields=('EmployeeId', 'EmployeeName', 'Department', 'DateOfJoining', 'PhotoFileName',)
        


