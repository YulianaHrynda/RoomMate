from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RoomForm
from .forms import EnterRoomForm
from .models import Room
from userprofile.models import Profile

@login_required
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            profile = request.user.profile
            profile.rooms.add(room)
            return redirect('profile')  # Redirect to the profile page after creation
    else:
        form = RoomForm()
    return render(request, 'create_room.html', {'form': form})

@login_required
def enter_room(request):
    if request.method == 'POST':
        form = EnterRoomForm(request.POST)
        if form.is_valid():
            room_id = form.cleaned_data['room_id']
            try:
                room = Room.objects.get(room_id=room_id)
                profile = Profile.objects.get(user=request.user)
                profile.rooms.add(room)
                return redirect('profile')  # Assuming you have a profile page
            except Room.DoesNotExist:
                form.add_error('room_id', 'Room with this key does not exist.')
    else:
        form = EnterRoomForm()

    return render(request, 'enter_room.html', {'form': form})