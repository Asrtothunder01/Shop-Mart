from .models import Product

from django.contrib import admin

@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_filter = ('name','price')
    
    list_display = ('name','price')
    
    search_fields = ('name','price__stock')
    
    date_hierarchy = 'created_at'
    
    
    
  