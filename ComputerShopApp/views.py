from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from ComputerShopApp.serializers import UserSerializer
from ComputerShopApp.models import User

# Create your views here.

@csrf_exempt
def userApi(request,id=0):
    if request.method=='GET':
        User = User.objects.all()
        User_serializer=UserSerializer(User,many=True)
        return JsonResponse(User_serializer.data,safe=False)
    elif request.method=='POST':
        User_data=JSONParser().parse(request)
        User_serializer=UserSerializer(data=User_data)
        if User_serializer.is_valid():
            User_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        User_data=JSONParser().parse(request)
        User=User.objects.get(id=id)
        User_serializer=UserSerializer(User,data=User_data)
        if User_serializer.is_valid():
            User_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        User=User.objects.get(id=id)
        User.delete()
        return JsonResponse("Deleted Successfully",safe=False)

