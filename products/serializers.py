from rest_framework import serializers
from .models import Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

    def validate(self, data):
        product = data['product']
        quantity = data['quantity']
        if quantity > product.stock:
            raise serializers.ValidationError(f"Not enough stock available for {product.name}.")
        return data

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['items', 'total_price', 'status']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        total_price = 0
        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']

            if quantity > product.stock:
                raise serializers.ValidationError(f"Not enough stock for {product.name}.")
            
            # Deduct stock
            product.stock -= quantity
            product.save()

            # Create OrderItem
            order_item = OrderItem.objects.create(order=order, product=product, quantity=quantity)

            # Calculate total price
            total_price += product.price * quantity

        # Update total price of the order
        order.total_price = total_price
        order.save()

        return order

