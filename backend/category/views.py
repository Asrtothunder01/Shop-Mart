from .serializers import CategorySerializer

from .models import Category

from rest_framework.generics import ListAPIView, CreateAPIView

from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema



@extend_schema(
  tags = ['Category'],
  responses = {201: CategorySerializer (many = True)},
)
class CategoryCreateView (CreateAPIView):
    queryset = Category.objects.all()
    
    serializer_class = CategorySerializer
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
  
      
# Category List View
  
@extend_schema(
  tags = ['Category'],
  responses = {200: CategorySerializer (many = True)},
)  
class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    
    serializer_class = CategorySerializer
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
    