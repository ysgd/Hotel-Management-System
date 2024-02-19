from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import RoomTypeSerializer
from .models import RoomType

# Create your views here.
class RoomTypeView(ModelViewSet):
  queryset = RoomType.objects.all()
  serializer_class = RoomTypeSerializer