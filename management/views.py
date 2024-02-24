from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from .serializers import RoomTypeSerializer, RoomSerializer
from .models import RoomType, Room
from rest_framework.response import Response

# Create your views here.
class RoomTypeView(ModelViewSet):
  queryset = RoomType.objects.all()
  serializer_class = RoomTypeSerializer
  
# class RoomView(ModelViewSet):
#   queryset = Room.objects.all()
#   serializer_class = RoomSerializer

class RoomView(GenericAPIView):
  queryset = Room.objects.all()
  serializer_class = RoomSerializer
  
  def get(self,request):
    room_objs = self.get_queryset()
    serializer = RoomSerializer(room_objs,many=True)
    return Response(serializer.data)
  
  def post(self,request):
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)
    
  