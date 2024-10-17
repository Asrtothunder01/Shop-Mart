from django.contrib import admin

from .models import WishList, WishListItem

@admin.register(WishList)

class WishListAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    
    list_display = ('user',)
    
    search_display = ('user__username')
 
  
    
        
@admin.register(WishListItem)    
      
class WishListItemAdmin(admin.ModelAdmin):
    
    list_filter = ('wishlist','product')
    
    list_display = ('wishlist','product')
    
    search_display  = ('wishlist__product')