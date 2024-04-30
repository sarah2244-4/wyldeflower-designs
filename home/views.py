from django.shortcuts import render, redirect
from products.models import Product, Category


def index(request):
    """
    View the index page
    """

    products = Product.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            

    current_sorting = f'{sort}_{direction}'

    recent_products = Product.objects.order_by('-date_added')[:8]
    most_viewed_products = Product.objects.order_by('-views')[:8]

    context = {
        'products': products,
        'current_sorting': current_sorting,
        'recent_products': recent_products,
    }

    return render(request, 'home/index.html', context)

def how_it_works(request):
    """
    View the how it works page
    """

    return render(request, 'home/how_it_works.html')