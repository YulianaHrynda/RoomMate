from django.urls import path
from . import views

urlpatterns = [
    path('create_room/', views.create_room, name='create_room'),
    path('enter_room/', views.enter_room, name='enter_room'),
]
