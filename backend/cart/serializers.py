from rest_framework import serializers

from .models import Cart, CartItem

from custom.serializer import CustomerSerializer

from product.serializer import ProductSerializer



class CartSerializer(serializers.ModelSerializer):
    
    user = CustomerSerializer (many = True)
    
    class Meta:
        model = Cart
        fields = ['id','user','created_at']
        read_only_fields = ['id','user']
   
             
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer ()
    
    class Meta:
        model = CartItem
        fields = ['id','cart','product','question']   
        
        
        