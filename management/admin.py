from django.contrib import admin
from .models import Room,RoomType,User
# Register your models here.
admin.site.register(User)
admin.site.register(Room)
admin.site.register(RoomType)