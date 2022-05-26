from django.shortcuts import render
from .forms import UserUpdateForm, ProfileUpdateForm


def ProfileViews(request):
    return render(request, 'user/profile.html')


def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    return render(request, 'user/profile.html', {'u_form': u_form, 'p_form': p_form})
