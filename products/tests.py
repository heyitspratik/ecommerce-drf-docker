import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product, Order

class ProductAndOrderTests(TestCase):
    def setUp(self):
        # Setup for both Product and Order
        self.client = APIClient()
        self.product_data = {
            "name": "Test Product",
            "description": "Test Description",
            "price": 10.0,
            "stock": 5
        }
        # Create a product to test against
        self.product = Product.objects.create(**self.product_data)
        self.order_data = {
            "products": [
                {"product": self.product.id, "quantity": 3}
            ],
            "total_price": 30.0,
            "status": "pending"
        }

    def test_create_product(self):
        response = self.client.post('/api/products', self.product_data, format='json')
        print("product created", self.product_data, "\n")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_products(self):
        response = self.client.get('/api/products')
        print("list of available products", json.dumps(response.data, indent=2), "\n")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_place_order(self):
        response = self.client.post('/api/orders', self.order_data, format='json')
        print(f"order successfully placed id:{self.product.id}, name:{self.product.name}, quantity:{self.order_data['products'][0]['quantity']}\n")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.product.refresh_from_db()
        print(f"The remaining quantity of product: {self.product.name} is {self.product.stock}\n")
        self.assertEqual(self.product.stock, 2)

    def test_order_with_insufficient_stock(self):
        self.order_data["products"][0]["quantity"] = 10
        print("Testing insufficient stock with data...", self.order_data["products"][0])
        response = self.client.post('/api/orders', self.order_data, format='json')
        print(response.data['error'], "\n")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
