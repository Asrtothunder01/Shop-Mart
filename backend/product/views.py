from .serializers import ProductSerializer

from .models import Product

from rest_framework.generics import ListAPIView, CreateAPIView

from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema



@extend_schema(
  tags = ['Product'],
  responses = {201: ProductSerializer (many = True)},
)
class ProductCreateView (CreateAPIView):
    queryset = Product.objects.all()
    
    serializer_class = ProductSerializer
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
  
      
#Product List View
  
@extend_schema(
  tags = ['Product'],
  responses = {200: ProductSerializer (many = True)},
)  
class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    
    serializer_class = ProductSerializer
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
    