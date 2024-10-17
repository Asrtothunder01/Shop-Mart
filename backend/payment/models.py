from django.db import models

from order.models import Order

from custom.models import CustomUser


class BaseModel(models.Model):
    id = models.UUIDField(unique = True, default = uuid.uuid4, editable = False, primary_key = True) 
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        
        abstract = True
        

class Payment(BaseModel):
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
    
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    
    payment_method = models.Charfield(max_length = 100)
    
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    
    payment_status = models.CharField(max_length = 100, default = 'pending')
    
    
    def __str__(self):
        return f"Payment of {self.amount} for Order {self.order.id}"
    
    
    