from rest_framework import serializers

from .models import Cart


class CartSerializers(serializers.ModelSerializer):
    
    user = CustomerSerializer (many = True)
    
    class Meta:
        model = Cart
        fields = ['id','user','created_at']
        read_only_fields = ['id','user']