import jwt
from rest_framework import status
from backend.settings import SECRET_KEY
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.contrib.auth.models import User
from .models import Box
from .serializers import BoxSerializer
from rest_framework.response import Response
from .filters import BoxFilter,BoxUserFilter
from django.core.exceptions import ValidationError
# Create your views here.

class CreateBoxView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser,)

    def post(self,request):
        token=request.META['HTTP_AUTHORIZATION'].split(" ")[1]
        username=jwt.decode(token,SECRET_KEY, algorithms=['HS256'])['user_id']
        user=User.objects.get(username=username)
        serializer=BoxSerializer(data=request.data, context={'user': user})
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({"message":e},status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UpdateBoxView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)

    def put(self, request, pk):
        try:
            box = Box.objects.get(pk=pk)
        except Box.DoesNotExist:
            return Response({"message":"Box id specified does not exist"},status=status.HTTP_404_NOT_FOUND)

        serializer = BoxSerializer(box, data=request.data, partial=True)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({"message":e},status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AllBoxView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        boxes=Box.objects.all()
        filter_set = BoxFilter(request.GET, queryset=boxes)
        filtered_queryset = filter_set.qs
        serializer=BoxSerializer(filtered_queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class UserBoxView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)

    def get(self,request):
        token=request.META['HTTP_AUTHORIZATION'].split(" ")[1]
        username=jwt.decode(token,SECRET_KEY, algorithms=['HS256'])['user_id']
        user=User.objects.get(username=username)
        boxes=Box.objects.filter(creator=user.id)
        filter_set = BoxUserFilter(request.GET, queryset=boxes)
        filtered_queryset = filter_set.qs
        serializer=BoxSerializer(filtered_queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class BoxDeleteView(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)

    def delete(self,request,pk):
        token=request.META['HTTP_AUTHORIZATION'].split(" ")[1]
        username=jwt.decode(token,SECRET_KEY, algorithms=['HS256'])['user_id']
        user=User.objects.get(username=username)
        try:
            box = Box.objects.get(pk=pk)
            if box.creator.id==user.id:
                try:
                    box.delete()
                    return Response({"message":"Box Deleted"},status=status.HTTP_200_OK)
                except ValidationError as e:
                    return Response({"message":e},status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response({"message":"only creator allowed to delete"},status=status.HTTP_403_FORBIDDEN)
        except Box.DoesNotExist:
            return Response({"message":"Box id specified does not exist"},status=status.HTTP_404_NOT_FOUND)
        
        