from django.db import admin

from .models import Order, OrderItem

@admin.register(Order)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','status')
    
    list_filter = ('user','status')
    
    date_hierarchy = 'created_at'
    
    search_fields = ('user','status')
    
@admin.register(OrderItem)

class OrderItem (admin.ModelAdmin):
    list_display = ('order','product')
    
    list_filter = ('order','product')
    
    date_hierarchy = 'created_at'
    
    search_fields = ('order','product__name')