from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def view_profile(request):
    """
    View the profile page
    """
    return render(request, 'profile.html')