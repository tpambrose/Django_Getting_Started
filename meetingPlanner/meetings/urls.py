from django.urls import path,include

from .views import getMeeting,rooms

urlpatterns = [
    path("<int:id>",getMeeting,name="meeting"),
    path("rooms",rooms,name="rooms"),
]
