from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_people', 'room_id')
    search_fields = ('name', 'room_id')
