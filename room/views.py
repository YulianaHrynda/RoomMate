from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RoomForm

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
