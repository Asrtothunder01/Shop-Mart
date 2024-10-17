from django.contrib import admin

from .models import CustomUser

@admin.register(CustomUser)

class CustomUserAdmin(admin.ModelAdmin):
    list_filter = ('is_admin','is_customer')
    
    list_display = ('is_admin','is_customer')
    
    search_fields = ('is_admin__is_customer',)
