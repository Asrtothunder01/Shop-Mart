from rest_framework.generics import ListAPIView, CreateAPIView

from rest_framework.permissions import IsAuthenticated

from .serializers import CartSerializers

from .models import Cart

from drf_spectacular.utils import extend_schema


@extend_schema(
  tags = ['Cart'],
  responses = {200: CartSerializers (many = True)},
)

class CartListView(ListAPIView):
    queryset = Cart.objects.all()
    
    serializer_class = CartSerializers
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
    


@extend_schema(
  tags = ['Cart'],
  responses = {201: CartSerializers (many = True)},
)

class CartCreateView(CreateAPIView):
    queryset = Cart.objects.all()
    
    serializer_class = CartSerializers
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
    
    