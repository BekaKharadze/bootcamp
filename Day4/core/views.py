from django.shortcuts import render
from django.db import transaction
from .models import Order, OrderItem  # Ensure these models are imported

@transaction.atomic
def create_order_and_items(order_data, items_data):
    order = Order.objects.create(**order_data)  # Ensure order_data has correct fields
    
    for item in items_data:
        OrderItem.objects.create(order=order, **item)  # Ensure item contains correct fields
