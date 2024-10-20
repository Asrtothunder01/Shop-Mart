from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(unique = True, default = uuid.uuid4, editable = False, primary_key = True) 
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        
        abstract = True
        
        
class Category(BaseModel):
    name  = models.CharField(max_length = 255)
    
    description = models.TextField()
    
    slug = models.SlugField(unique = True)
    
    def __str__(self):
        return self.name
    