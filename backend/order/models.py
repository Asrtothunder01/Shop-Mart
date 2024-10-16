from django.db import models

from product.models import Product

from custom.models import CustomUser




class BaseModel(models.Model):
    id = models.UUIDField(unique = True, default = uuid.uuid4, editable = False, primary_key = True) 
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        
        abstract = True
        



class Order(BaseModel):
    
    ORDER_STATUS =(
      ('Pending', 'Pending'),
      ('Shipped'),('Shipped'),
      ('Delivered'),('Delivered'),
      ('Cancelled'),('Cancelled'),
)
    
    
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
    
    status = models.CharField(max_length = 20, choices = ORDER_STATUS, default = 'pending')
    
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
        



class OrderItem(BaseModel):
    
    order = models.ForeignKey(Order,on_delete = models.CASCADE)
    
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    
    quantity = models.PositiveIntegerField()
    
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    
    def __str__(self):
        return f"{self.quantity}x{self.product.name}"
        