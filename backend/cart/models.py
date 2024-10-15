from django.db import models

from custom.models import CustomUser

# Cart Model

class Cart(models.Models):
    id = models.UUIDField(editable = False, unique = True, primary_key = True, ddefault = uuid.uuid4)
    
    user = models.OneToOneField(CustomUser,on_delete = models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    return f"Cart For {self.user.username}"
    
    