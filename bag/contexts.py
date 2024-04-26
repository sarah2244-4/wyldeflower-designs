from django.conf import settings
from django.shortcuts import get_object_or_404
from decimal import Decimal

from products.models import Product

def bag_contents(request):

    bag_items = []
    total = Decimal('0')
    product_count = 0
    subtotal = Decimal('0')
    delivery_price = Decimal('0')
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        subtotal += quantity * product.price
        total += subtotal
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'subtotal': subtotal,
        })

        if product.categories == 'printable':
            delivery = Decimal(delivery_price)
        else:
            delivery = Decimal(settings.STANDARD_DELIVERY_PRICE)
    grand_total = total + delivery
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
        'subtotal': subtotal,
    }

    return context