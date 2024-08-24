from django.contrib import admin
from .models import Profile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'list_rooms')  # Replace 'rooms' with 'list_rooms'

    def list_rooms(self, obj):
        return ", ".join([room.name for room in obj.rooms.all()])

    list_rooms.short_description = 'Rooms'

admin.site.register(Profile, UserProfileAdmin)
