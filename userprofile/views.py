from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm

# Create your views here.

@login_required
def profile_view(request):
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')  # Replace 'profile' with the name of your profile page's URL
    else:
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profile.html', {'profile_form': profile_form})
