from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit/<int:user_id>/', views.edit_profile, name='edit_profile'),
    path('add/<int:product_id>/<slug>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
]