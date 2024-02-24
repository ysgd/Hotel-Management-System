from rest_framework import serializers
from .models import RoomType,Room

class RoomTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = RoomType
    fields = '__all__'
    
class RoomSerializer(serializers.ModelSerializer):
  class Meta:
    model = Room
    fields = '__all__'