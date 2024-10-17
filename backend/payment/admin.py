from .models import Payment

from django.contrib import admin

@admin.register(Payment)

class PaymentAdmin(admin.ModelAdmin):
    list_filter = ('order','payment_status')
    
    list_display = ('order','payment_method','amount','payment_status')
    
    search_fields = ('amount','payment_method__order')
    
    date_hierarchy = 'created_at'
    
    
    
  