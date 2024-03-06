from rest_framework import serializers
from .models import Hive, Task

class HiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hive
        fields = ['id', 'hiveTitle', 'hiveDescription', 'intendedUsers', 'hiveStartDate', 'hiveEndDate', 'status',]

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'taskTitle', 'taskDescription', 'taskStartDate', 'taskEndDate', 'assignedTo']

