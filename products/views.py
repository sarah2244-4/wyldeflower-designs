from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Category, Product, ProductImage
from .forms import ProductForm
from profiles.forms import AddToWishlistForm
from profiles.models import Wishlist


def all_products(request):
    """ 
    A view to show all products, including sorting and search queries 
    """

    products = Product.objects.all()
    query = None
    categories = None
    types = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'type':
                sortkey = 'type__name'

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/product_list.html', context)


def product_detail(request, product_id, slug):
    """
    A view to show individual product details
    """

    product = get_object_or_404(Product, pk=product_id)
    images = product.images.all()
    
    # Increment view count
    product.views += 1
    product.save()

    context = {
        'product': product,
        'images': images,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ 
    A view for an admin to add an product to the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)

        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.slug = unique_slug_generator(product)
            product.save()

            # Save cover image
            cover_image = request.FILES.get('cover_image')
            if cover_image:
                ProductImage.objects.create(product=product, image=cover_image, is_cover=True)

            # Handle additional images
            for file in request.FILES.getlist('images'):
                ProductImage.objects.create(product=product, image=file, is_cover=False)
            
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id, product.slug]))
        
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')

    else:
        product_form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'product_form': product_form,
    }
    
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    A view for an admin to edit an product in the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    A view for an admin to delete an product completely from the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))

@login_required
def add_to_wishlist(request):
    if request.method == 'POST':
        form = AddToWishlistForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            slug = form.cleaned_data['slug']
            product = get_object_or_404(Product, id=product_id, slug=slug)
            wished_product, created = Wishlist.objects.get_or_create(
                wished_product=product,
                user=request.user,
            )
            if created:
                messages.success(request, 'The item was added to your wishlist.')
            else:
                messages.info(request, 'The item is already in your wishlist.')
        else:
            messages.error(request, 'Failed to add to wishlist. Invalid data.')
    return redirect(request.META.get('HTTP_REFERER', 'product_list'))


def unique_slug_generator(instance, new_slug=None):
    slug = new_slug or slugify(instance.name)
    Klass = instance.__class__
    if Klass.objects.filter(slug=slug).exists():
        new_slug = f"{slug}-{Klass.objects.filter(slug=slug).count() + 1}"
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug