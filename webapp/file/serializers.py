from rest_framework import serializers
from .models import Employee_Task

class EmployeetaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_Task
        fields = "__all__"