from rest_framework import serializers
from .models import Hive, Task

# Create HiveSerializers to convert object into json
class HiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hive
        fields = ['id', 'hiveTitle', 'hiveDescription', 'intendedUsers', 'hiveStartDate', 'hiveEndDate', 'status',]


# Create TaskSerializers to convert object into json
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'taskTitle', 'taskDescription', 'taskStartDate', 'taskEndDate', 'assignedTo']


