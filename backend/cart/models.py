from django.db import models

from custom.models import CustomUser

from product.models import Product


# Cart Model
class BaseModel(models.Model):
    id = models.UUIDField(unique = True, default = uuid.uuid4, editable = False, primary_key = True) 
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        
        abstract = True



class Cart(BaseModel):
    
    user = models.OneToOneField(CustomUser,on_delete = models.CASCADE)
    def __str__(self):
        return f"Cart For {self.user.username}"
    


class CartItem(BaseModel):
    
    cart = models.ForeignKey(Cart,on_delete = models.CASCADE)
    
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    
    quantity = models.IntegerField(default = 1)
    
    def __str__(self):
        return f"{self.quantity}x{self.product.name}"
    
    