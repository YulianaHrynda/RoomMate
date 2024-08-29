from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'number_of_people']

class EnterRoomForm(forms.Form):
    room_id = forms.UUIDField(label="Key of the room")
