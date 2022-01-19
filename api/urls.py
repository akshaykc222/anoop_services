from django.contrib import admin
from django.urls import path, include
from .views import (BusinessApiView  
            ,AppointmentApiView,UserApiView,FeedBackApiView,TimeSlotApi)
from rest_framework.schemas import get_schema_view
urlpatterns = [
   
    # path('users/',UserApiView.as_view(),name="users"),
    path('business/',BusinessApiView.as_view(),name="business"),
    path('business/<int:id>/',BusinessApiView.as_view(),name="business"),
 path('business/<int:id>/<int:user>/',BusinessApiView.as_view(),name="business"),
    path('appointments/',AppointmentApiView.as_view(),name="appointments"),
    path('appointments/<int:id>/',AppointmentApiView.as_view(),name="appointments"),
    path('appointments/<int:id>/<int:user>/',AppointmentApiView.as_view(),name="appointments"),
   
    path('users/',UserApiView.as_view(),name="users"),
    path('timeslots/',TimeSlotApi.as_view(),name="users"),
    path('timeslots/<int:id>/',TimeSlotApi.as_view(),name="users"),
    path('users/<int:id>/',UserApiView.as_view(),name="users"),
    path('feedback/',FeedBackApiView.as_view(),name="feedback"),
   
  
 path('openapi/', get_schema_view(
        title="perfect api",
        description=""
    ), name='openapi-schema'),
]
