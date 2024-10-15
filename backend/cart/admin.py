from django.contrib import admin

from .models import Cart,CartItem

@admin.register(Cart)

class CartAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    
    list_display = ('user',)
    
    date_hierarchy = 'created_at'
    
    search_fields = ('user__username',)

    
@admin.register(CartItem)            
class CartItemAdmin (admin.ModelAdmin):
    list_filter = ('cart',)
    
    list_display = ('product', 'quantity')
    
    date_hierarchy = 'created_at'
    
    search_fields = ('cart','product__name')