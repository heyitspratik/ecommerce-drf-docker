from django.urls import path
from .views import ProductListCreateView, OrderCreateView

urlpatterns = [
    path('products', ProductListCreateView.as_view(), name='product-list-create'),
    path('orders', OrderCreateView.as_view(), name='order-create'),
]
