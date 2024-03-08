from django.http import JsonResponse
from .models import User, Hive, Task, Membership
from .serializers import UserSerializer, HiveSerializer, TaskSerializer, MembershipSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# from rest_framework import serializers



# @api_view(['POST'])
# def UserLogin(request):
#     return Response({})

# @api_view('GET', 'POST')
# def UserSignUp(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         user = User.objects.get(username=request.data['username'])
#         user.set_password(request.data['password'])
#         user.save()
#         token = Token.objects.create(user=user)
#         return Response({"token": token.key, "user": serializer.data})

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def test_token(request):
#     return Response({})


def User_list(request):
    # get all the HiveObjects
    UserObjects = User.objects.all()

    # serialize the object
    serializeObject = UserSerializer(UserObjects, many=True)
    # return Json
    return JsonResponse({'UserCreated': serializeObject.data})


def Hive_list(request):
    # get all the HiveObjects
    HiveObjects = Hive.objects.all()

    # serialize the object
    serializeObject = HiveSerializer(HiveObjects, many=True)
    # return Json
    return JsonResponse({'hiveCreated': serializeObject.data})


@api_view(['GET', 'POST'])
def Task_list(request):

    if request.method == 'GET':
        # get all the HiveObjects
        TaskObjects = Task.objects.all()

        # serialize the object
        serializeObject = TaskSerializer(TaskObjects, many=True)
        # return Json
        return JsonResponse({'taskCreated': serializeObject.data})

    if request.method == 'POST':
        # serialize the object
        serializeObject = TaskSerializer(data=request.data)
        if serializeObject.is_valid():
            serializeObject.save()
            # return Json
            return Response(serializeObject.data, status=status.HTTP_201_CREATED)


def Membership_list(request):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) ignore
    # get all the HiveObjects
    MembershipObjects = Membership.objects.all()

    # serialize the object
    serializeObject = MembershipSerializer(MembershipObjects, many=True)
    # return Json
    return JsonResponse({'members': serializeObject.data})

