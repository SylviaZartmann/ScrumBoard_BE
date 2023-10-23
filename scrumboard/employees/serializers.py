from rest_framework import serializers
from employees.models import Employee

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['url', 'firstname', 'lastname', 'email', 'phone', 'origin_city', 'origin_street', 'origin_post_code', 'profession', 'entry_date', 'leaving_date', 'working_hours', 'salary', 'color', 'current_project']