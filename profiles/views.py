from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order
from profiles.models import Wishlist
from products.models import Product


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = Order.objects.filter(user_profile=profile)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def edit_profile(request, user_id):
    """ Edit the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = Order.objects.filter(user_profile=profile)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/edit_profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id, slug):
    product = get_object_or_404(Product, id=product_id, slug=slug)

    if request.method == 'POST':
        wished_product, created = Wishlist.objects.get_or_create(
            wished_product=product,
            user=request.user,
        )
        if created:
            messages.success(request, 'The item was added to your wishlist')
        else:
            messages.info(request, 'The item is already in your wishlist')
    else:
        messages.error(request, 'Update failed. Please ensure the form is valid.')

    return redirect(reverse('product_detail', args=[product_id, slug]))