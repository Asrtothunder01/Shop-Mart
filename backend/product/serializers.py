from rest_framework import serializers

from .models import Product

class ProductSerializer (serializers.ModelSerializer):
     
     category = CategorySerializer()
     
     class Meta:
         model = Product
         
         fields = ['id','name','price','description','stock','image','category','slug']
     