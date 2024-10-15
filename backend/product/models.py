from django.db import models

from category.models import Category


class BaseModel(models.Model):
    id = models.UUIDField(unique = True, default = uuid.uuid4, editable = False, primary_key = True) 
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        
        abstract = True
        
        
class Product(BaseModel):
    name  = models.CharField(max_length = 255)
    
    price = models.DecimalField(max_digits = 25, decimal_places = 2)
    
    description = models.TextField()
    
    stock = models.PositiveIntegerField()
    
    category = models.ForeignKey(Category,on_delete = models.SET_NULL,null = True)
    
    image = models.ImageaField(upload_to = 'product_image/', blank = True,null = True)
    
    slug = models.SlugField(unique = True)
    
    
    def __str__(self):
        return self.name