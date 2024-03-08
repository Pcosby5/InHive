from rest_framework import serializers
from .models import User, Hive, Task, Membership


# Create UserSerializers to convert object into json
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

# Create HiveSerializers to convert object into json
class HiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hive
        fields = ['id', 'hiveTitle', 'hiveDescription', 'intendedUsers', 'hiveStartDate', 'hiveEndDate', 'status', 'HiveOwner']


# Create TaskSerializers to convert object into json
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'taskTitle', 'taskDescription', 'taskStartDate', 'taskEndDate', 'assignedTo', 'hive']


# Create MembershipSerializers to convert object into json
class MembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership
        # got rid of user field because i have not authenticated it yet
        # plus i have not created a meta class for User model yet
        # gotta authorize users to perform admin
        # hence gotta serializeUser
        fields = ['id', 'User', 'hive', 'role']




