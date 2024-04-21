from django.test import TestCase
from django.contrib.auth.models import User
from .models import  Order, OrderItem


# Integration Tests

class OrderItemIntegrationTestCase(TestCase):
    def test_order_item_order_integration(self):
        # Create a user
        user = User.objects.create_user(username='testuser', password='password')
        
        # Create an order associated with the user
        order = Order.objects.create(user=user)

        # Now create an order item associated with the order
        order_item = OrderItem.objects.create(order=order)
    
