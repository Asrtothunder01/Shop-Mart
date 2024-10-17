from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(unique = True, default = uuid.uuid4, editable = False, primary_key = True) 
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        
        abstract = True
        
        
class Review (BaseModel):
    
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
    
    rating = models.PositiveIntegerField()
    
    comment = models.TextField(blank = True,null = True)
    
    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"