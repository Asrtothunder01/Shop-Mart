from django.contrib import admin

from .models import Review

@admin.register(Review)

class ReviewAdmin(admin.ModelAdmin):
    list_filter = ('user','product')
    
    list_display = ('product','rating')
    
    search_fields = ('user__product.name',)
