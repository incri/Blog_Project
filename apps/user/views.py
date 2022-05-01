from django.shortcuts import render


def ProfileViews(request):
    return render(request, 'user/profile.html')
