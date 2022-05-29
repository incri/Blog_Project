from django.shortcuts import render, redirect
from .forms import UserUpdateForm, ProfileUpdateForm


def ProfileViews(request):
    return render(request, 'user/profile.html')


def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile-page')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'user/profile.html', {
                                            'u_form': u_form, 'p_form': p_form
                                                    })
