from rest_framework import serializers
from .models import RoomType,Room, User
from django.contrib.auth.models import Group

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = ['id','name']

class RoomTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = RoomType
    fields = '__all__'
    
class RoomSerializer(serializers.ModelSerializer):
  class Meta:
    model = Room
    fields = '__all__'
    
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['email','password','groups']