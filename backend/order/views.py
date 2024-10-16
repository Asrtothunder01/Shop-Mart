from rest_framework.generics import ListAPIView, CreateAPIView

from .serializers import OrderSerializer, OrderItemSerializer

from .models import Order, OrderItem

from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema


# Order List Views

@extend_schema(
  tags = ['Order'],
  responses = {200: OrderSerializer (many = True)},
)
class OrderListView(ListAPIView):
    
    queryset = Order.objects.all()
    
    pagination_class = None
    
    serializer_class = OrderSerializer
    
    permission_classes = [IsAuthenticated]




#Order Create View

@extend_schema(
 tags = ['Order'],
 
 responses = {201: OrderSerializer (many = True)},

)   
class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    
    serializer_class = OrderSerializer
    
    pagination_class = None
    
    permission_class = [IsAuthenticated]
    


#Order Item Create View

@extend_schema(
 tags = ['OrderItem'],
 responses = {201: OrderItemSerializer (many = True)},
)
class OrderItemCreateView (CreateAPIView):
    
    queryset = OrderItem.objects.all()
    
    pagination_class = None
    
    serializer_class = OrderItemSerializer
    
    permission_classes = [IsAuthenticated]
    


#Order Item List View

@extend_schema(
 tags = ['OrderItem'],
 
 responses = {200: OrderItemSerializer (many =  True)},
  
)

class OrderItemListView(ListAPIView):
    
    queryset = OrderItem.objects.all()
    
    pagination_class = None
    
    serializer_class = OrderItemSerializer
    
    permission_classes = [IsAuthenticated]