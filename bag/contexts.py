from django.conf import settings
from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.db.models import Sum

from products.models import Product

def bag_contents(request):

    bag_items = []
    total = Decimal('0')
    product_count = 0
    subtotal = Decimal('0')
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        subtotal = quantity * product.price
        total += subtotal
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'subtotal': subtotal,
            'total': total,
        })

    for item in bag_items:
        non_printable_total = Decimal('0')
        printable_total = Decimal('0')
        if 'printable' not in item['product'].categories.values_list('name', flat=True):
            non_printable_total += item['subtotal']
        else:
            printable_total += item['subtotal']

        # Free delivery over threshold
        if printable_total == total:
            delivery_cost = Decimal('0')
        elif total < Decimal(settings.FREE_DELIVERY_THRESHOLD):
            delivery_cost = Decimal(settings.STANDARD_DELIVERY_PRICE)
        else:
            delivery_cost = Decimal('0')

    grand_total = total + delivery_cost
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery_cost': delivery_cost,
        'grand_total': grand_total,
        'subtotal': subtotal,
    }

    return context