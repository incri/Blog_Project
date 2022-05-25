from django.shortcuts import render
from .forms import UserUpdateForm, ProfileUpdateForm


def ProfileViews(request):
    return render(request, 'user/profile.html')


def Profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user/profile.html', context)

