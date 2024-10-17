from rest_framework import serializers

from .models import Payment


class PaymentSerializer (serializers.ModelSerializer):
    user = CustomUserSerializer ()
    order = OrderSerializer ()
    
    class Meta:
        model = Payment
        
        fields = ['id','user','payment_status','order','payment_method','amount','created_at','updated_at']
        
        read_only_fields = ['id','user','payment_status','created_at','updated_at']
        
        