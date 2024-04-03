from django.shortcuts import render, redirect
from .forms import NewsletterSignupForm


def index(request):
    """
    View the index page
    """
    return render(request, 'home/index.html')


def newsletter_signup_view(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save(request)
            return redirect('home')
    else:
        form = NewsletterSignupForm()
    return render(request, 'signup.html', {'form': form})