from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

class ProductListCreateView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderCreateView(APIView):
    def post(self, request):
        data = request.data
        products_data = data.get('products', [])
        total_price = 0
        for item in products_data:
            try:
                product = Product.objects.get(id=item['product'])
                if product.stock < item['quantity']:
                    return Response({'error': f"Insufficient stock for {product.name}, available quantity is {product.stock}"}, status=status.HTTP_400_BAD_REQUEST)
                total_price += product.price * item['quantity']
            except Product.DoesNotExist:
                return Response({'error': f"Product ID {item['id']} not found."}, status=status.HTTP_404_NOT_FOUND)

        order = Order.objects.create(products=products_data, total_price=total_price)
        for item in products_data:
            product = Product.objects.get(id=item['product'])
            product.stock -= item['quantity']
            product.save()

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
