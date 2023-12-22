from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('fullremove/<int:product_id>/', views.full_remove, name='full_remove'),


    
]