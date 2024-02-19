from rest_framework import serializers
from .models import RoomType

class RoomTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = RoomType
    fields = '__all__'