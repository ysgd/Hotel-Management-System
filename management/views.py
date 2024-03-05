from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from .serializers import RoomTypeSerializer, RoomSerializer, UserSerializer
from .models import RoomType, Room, User
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny
from rest_framework import filters


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
  filterset_fields = ['type']
  search_fields = ['name']
  
  def get(self,request):
    room_objs = self.get_queryset()
    filter_objs = self.filter_queryset(room_objs)
    serializer = RoomSerializer(filter_objs,many=True)
    return Response(serializer.data)
  
  def post(self,request):
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)
    
class RoomEditView(GenericAPIView):
  queryset = Room.objects.all()
  serializer_class = RoomSerializer
  
  def get(self,request,pk):
    room_obj = Room.objects.get(id=pk)
    serializer = RoomSerializer(room_obj)
    return Response(serializer.data)
  
  def put(self,request,pk):
    room_obj = Room.objects.get(id=pk)
    serializer = RoomSerializer(room_obj,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)
    
  def delete(self,request,pk):
    room_obj = Room.objects.get(id=pk)
    room_obj.delete()
    return Response("data deleted")

  
class UserView(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [AllowAny]
  
  def register(self,request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      password = request.data.get('password')
      hash_password = make_password(password)
      serializer.save(hash_password)
      return Response("user created")
    else:
      return Response(serializer.errors)
    
  def login(self,request):
    username = request.data.get('email')
    password = request.data.get('password')
    
    user = authenticate(username='email',password='password')
    
    if user == None:
      return Response('invalid credentials')
    else:
      token,_= Token.objects.get_or_create(user=user)
      return Response(token)
      
  
  