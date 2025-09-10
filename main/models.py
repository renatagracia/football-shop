import uuid
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.category}"
    
    @property
    def is_expensive(self):
        return self.price > 1000000
