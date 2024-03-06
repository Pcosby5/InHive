from django.http import JsonResponse
from .models import Hive, Task
from .serializers import HiveSerializer, TaskSerializer, MembershipSerializer


def Hive_list(request):
    # get all the HiveObjects
    HiveObjects = Hive.objects.all()

    # serialize the object
    serializeObject = HiveSerializer(HiveObjects, many=True)
    # return Json
    return JsonResponse({'hiveCreated': serializeObject.data})

def Task_list(request):
    # get all the HiveObjects
    TaskObjects = Task.objects.all()

    # serialize the object
    serializeObject = TaskSerializer(TaskObjects, many=True)
    # return Json
    return JsonResponse({'taskCreated': serializeObject.data})

def Membership_list(request):
    # get all the HiveObjects
    TaskObjects = Task.objects.all()

    # serialize the object
    serializeObject = MembershipSerializer(TaskObjects, many=True)
    # return Json
    return JsonResponse({'members': serializeObject.data})

