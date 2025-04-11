from rest_framework import serializers
from student.models import Student
from employee.models import Employee
from django.db import models 

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def validate(self, data):
        # Dynamically get the allowed fields from the model
        print(f"data in valida {data}")
        allowed_field_names = {field.name for field in Employee._meta.get_fields() if isinstance(field, models.Field)}
        print(allowed_field_names)
        # Check for extra fields in the incoming data
        extra_fields = set(data.keys()) - allowed_field_names
        print(extra_fields)
        
        if extra_fields:
            raise serializers.ValidationError(f"Unexpected fields: {', '.join(extra_fields)}")

        return data