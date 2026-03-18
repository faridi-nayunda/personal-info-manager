from django.db import models
from django.contrib.auth.models import User

class Information(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=150)
    date_of_birth = models.DateField(unique=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    document_file = models.FileField(upload_to='documents/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  

    def __str__(self):
        return self.first_name



# # Order view
# from rest_framework import permissions
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.viewsets import ModelViewSet
# from .models import Order
# from .serializers import OrderSerializer

# class OrderViewSet(ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         if self.request.user.is_staff:
#             return Order.objects.all()
#         return Order.objects.filter(user=self.request.user)

#     def create(self, request, *args, **kwargs):
#         cart_items = CartItem.objects.filter(user=request.user)
        
#         if not cart_items.exists():
#             return Response(
#                 {"detail": "Your cart is empty"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         # Calculate total price
#         total_price = sum(item.total_price() for item in cart_items)
        
#         # Create the order
#         order = Order.objects.create(
#             user=request.user,
#             total_price=total_price,
#             status='Pending'
#         )
        
#         # Create order items from cart items
#         for cart_item in cart_items:
#             OrderItem.objects.create(
#                 order=order,
#                 product=cart_item.product,
#                 quantity=cart_item.quantity,
#                 price=cart_item.product.price  # Save price at time of purchase
#             )
        
#         # Clear the cart
#         cart_items.delete()
        
#         serializer = self.get_serializer(order)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
#     # For admin
#     @action(detail=True, methods=['patch'])
#     def update_status(self, request, pk=None):
#         """
#         Custom action to update the order status.
#         Admin can update any order status.
#         """
#         order = self.get_object()
        
#         # Only allow updates to the status if the user is admin
#         if not request.user.is_staff:
#             return Response({"detail": "You do not have permission to perform this action."},
#                             status=status.HTTP_403_FORBIDDEN)
        
#         # Update order status
#         status = request.data.get('status')
#         if status not in ['completed', 'cancelled', 'pending']:  # Valid statuses
#             return Response({"detail": "Invalid status value."}, status=status.HTTP_400_BAD_REQUEST)
        
#         order.status = status
#         order.save()

#         return Response(OrderSerializer(order).data)