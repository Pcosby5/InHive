from rest_framework import serializers
from .models import Hive

class HiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hive
        fields = ['id', 'hiveTitle', 'hiveDescription', 'intendedUsers', 'hiveStartDate', 'hiveEndDate', 'status',]
