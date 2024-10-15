from django.contrib.auth.models import AbstractUser

from django.db import models

class CustomUser(AbstractUser):
    id = models.UUIDField(editable = False, unique = True, primary_key = True, ddefault = uuid.uuid4)
    
    is_customer = models.BooleanField(default = False)
    
    is_admin = models.BooleanField(default = False)
    
    