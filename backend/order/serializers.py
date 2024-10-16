from rest_framework import serializers

from .models import Order, OrderItem


class OrderSerializer (serializers.ModelSerializer):
    
    user = CustomUserSerializer ( many = True)
    
    class Meta:
        model = Order
        fields = ['id','user','status','created_at','updated_at']   
        read_only_fields = ['id','user']  
        
           

class OrderItemSerializer(serializers.ModelSerializer):
    
       product = ProductSerializer()
       
       order = OrderSerializer()  
       
       class Meta:
            model = OrderItem
            fields = ['id', 'product','order','price','quantity','created','updated_at']
            read_only_fields = ['id','order','price']
             