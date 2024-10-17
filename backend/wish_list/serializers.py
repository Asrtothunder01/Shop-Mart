from rest_framework import serializers

from .models import WishList, WishListItem


class WishListSerializer(serializers.ModelSerializer):
    
    user = CustomUserSerializer ()
    
    class Meta:
        model = WishList
        
        fields = ['id','user']
        
class WishListItemSerializer(serializers.ModelSerializer):
    
    wishlist = WishListSerializer()
    
    product = ProductSerializer()
    
    class Meta:
        model = WishListItem
        
        fields = ['id','wishlist','product']
        
    