from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company (models.Model):
    created_by =models.ForeignKey(User, on_delete= models.CASCADE, related_name="companies")
    
    name = models.CharField(max_length=255),
    website = models.URLField(blank=True, null=True),
    location = models.CharField(blank= True, null=True, max_length=255),
    description = models.TextField(blank=True, null=True)

    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

