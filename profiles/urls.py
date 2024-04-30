from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('add/<int:product_id>/<slug>/', views.add_to_wishlist, name='add_to_wishlist'),
]