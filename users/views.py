from django.shortcuts import render


def view_profile(request):
    """
    View the profile page
    """
    return render(request, 'profile.html')