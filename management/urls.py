from django.urls import path
from .views import RoomTypeView, RoomView, RoomEditView, UserView

urlpatterns = [
    path('room-type/',RoomTypeView.as_view({'get':'list','post':'create'})),
    path('room-type/<int:pk>/',RoomTypeView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('room/',RoomView.as_view()),
    path('room/<int:pk>/',RoomEditView.as_view()),
    path('register/',UserView.as_view({'post':'register'}),name='register'),
    path('login/',UserView.as_view({'post':'login'}),name='login')
]