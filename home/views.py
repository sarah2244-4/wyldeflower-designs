from django.shortcuts import render


def index(request):
    """
    View the index page
    """
    return render(request, 'home/index.html')