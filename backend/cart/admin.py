from django.contrib import admin

from .models import Cart


@admin.register(Cart)

class CartAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    
    list_filter = ('user',)
    
    date_hierarchy = 'created_at'
    
    search_fields = ('user__username',)