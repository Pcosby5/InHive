from django.http import JsonResponse
from .models import Hive
from .serializers import HiveSerializer


def Hive_list(request):
    # get all the HiveObjects
    HiveObjects = Hive.objects.all()

    # serialize the object
    serializeObject = HiveSerializer(HiveObjects, many=True)
    # return Json
    return JsonResponse({'hiveCreated': serializeObject.data})

