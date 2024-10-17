from django.db import models

from custom.models import CustomUser

from product.models import Product

class BaseModel(models.Model):
    id = models.UUIDField(unique = True, default = uuid.uuid4, editable = False, primary_key = True) 
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        
        abstract = True
        


class WishList (BaseModel):
    user = models.OneToOneField(CustomUser,on_delete = models.CASCADE)
    
    def __str__(self):
        return f"wishlist for {self.user.username}"
        


class WishListItem(BaseModel):
    wishlist = models.ForeignKey(WishList,on_delete = models.CASCADE)
    
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    
    def __str__(self):
        return f"{self.product.name} in wishlist"