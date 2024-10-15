from rest_framework.generics import ListAPIView, CreateAPIView

from rest_framework.permissions import IsAuthenticated

from .serializers import CartSerializer, CartItemSerializer

from .models import Cart

from drf_spectacular.utils import extend_schema



# Cart View

@extend_schema(
  tags = ['Cart'],
  responses = {200: CartSerializer (many = True)},
)

class CartListView(ListAPIView):
    queryset = Cart.objects.all()
    
    serializer_class = CartSerializer
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
    


@extend_schema(
  tags = ['Cart'],
  responses = {201: CartSerializer (many = True)},
)

class CartCreateView(CreateAPIView):
    queryset = Cart.objects.all()
    
    serializer_class = CartSerializer
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
 
 
 
 
# CartItem  View
       
@extend_schema(
  tags = ['CartItem'],
  responses = {200: CartItemSerializer (many = True)},
) 
class CartItemListView (ListAPIView):
    
    queryset = CartItem.objects.all()   
    
    serializer_class = CartItemSerializer
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
    


@extend_schema(
  tags = ['CartIem'],
  
  responses = {201: CartItemSerializer (many = True)},
)
class CartItemCreateView(CreateAPIView):
    
    queryset = CartItem.objects.all()
    
    serializer_class = CartItemSerializer
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None