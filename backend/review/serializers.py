from rest_framework import serializers

from .models import Review


class ReviewSerializer (serializers.ModelSerializer):
    
    user = CustomUserSerializer ()
    
    product = ProductSerializer()
    
    class Meta:
        model = Review
        
        fields = ['id','user','product','rating','comment','created_at','updated_at']
        
        read_only_fields = ['id','user','product','rating']
        
        