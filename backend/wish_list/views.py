from rest_framework.generics import ListAPIView, CreateAPIView

from rest_framework.permissions import IsAuthenticated

from .models import WishList, WishListItem

from .serializers import WishListSerializer, WishListItemSerializer

from drf_spectacular.utils import extend_schema



@extend_schema(
 tags = ['wishlist'],
 responses = {200: WishListSerializer (many = True)},
)
class WishListView(ListAPIView):
    queryset = WishList.objects.all()
    
    serializer_class = WishListSerializer
    
    pagination_class = None
    
    permission_class = [IsAuthenticated]
    

    
@extend_schema(
  tags = ['WishList'],  
  
  responses = {201: WishListSerializer(many = True)},
)    
class WishListCreateView(CreateAPIView):
    
    queryset = WishList.objects.all()
    
    serializer_class = WishListSerializer
    
    pagination_class = None
    
    permission_class = [IsAuthenticated]
    
 
   
@extend_schema(
  tags = ['WishListItem'],
  
  responses = {200: WishListItemSerializer(many = True)},
)

class WishListItemListView (serializers.ModelSerializer):
    
    queryset = WishListItem.objects.all()
    
    pagination_class = None
    
    permission_class = [IsAuthenticated]
    
    serializer_class = WishListItemSerializer
    
    
@extend_schema(
 tags = ['WishListItem'],
 
 responses = {201: WishListItemSerializer (many = True)},
)

class WishListItemCreateView (serializers.ModelSerializer):
    
    queryset = WishListItem.objects.all()
    
    pagination_class = None
    
    serializer_class = WishListItemSerializer
    
    permission_classes = [IsAuthenticated]