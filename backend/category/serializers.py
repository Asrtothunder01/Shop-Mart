from rest_framework import serializers

from .models import Category

class CategorySerializer (serializers.ModelSerializer):
     
     class Meta:
         model = Product
         
         fields = ['id','name','description','slug']
     