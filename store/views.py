import jwt
from rest_framework import status
from backend.settings import SECRET_KEY
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Box
from user.serializers import UserSerializer
from .serializers import BoxSerializer
from rest_framework.response import Response
# Create your views here.

class CreateBoxView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        token=request.META['HTTP_AUTHORIZATION'].split(" ")[1]
        username=jwt.decode(token,SECRET_KEY, algorithms=['HS256'])['user_id']
        user=User.objects.get(username=username)
        serializer=BoxSerializer(data=request.data, context={'user': user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UpdateBoxView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        box = Box.objects.get(pk=pk)
        serializer = BoxSerializer(box, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AllBoxView(APIView):
    def get(self,request):
        boxes=Box.objects.all()
        serializer=BoxSerializer(boxes,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class UserBoxView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        token=request.META['HTTP_AUTHORIZATION'].split(" ")[1]
        username=jwt.decode(token,SECRET_KEY, algorithms=['HS256'])['user_id']
        user=User.objects.get(username=username)
        boxes=Box.objects.filter(creator=user.id)
        serializer=BoxSerializer(boxes,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class BoxDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self,request,pk):
        token=request.META['HTTP_AUTHORIZATION'].split(" ")[1]
        username=jwt.decode(token,SECRET_KEY, algorithms=['HS256'])['user_id']
        user=User.objects.get(username=username)
        box = Box.objects.get(pk=pk)
        print(box.creator.id,user.id)
        if box.creator.id==user.id:
            box.delete()
            return Response(status=status.HTTP_200_OK)
        return Response({"message":"only creator allowed to delete"},status=status.HTTP_403_FORBIDDEN)