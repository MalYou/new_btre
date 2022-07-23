from django.db import models
from django.conf import settings
from datetime import datetime

from core.models import Address

class Listing(models.Model):
    """ Model for listing objects """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=201)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self) -> str:
        return self.title


class Attachment(models.Model):
    """
        Manages attachment objects
    """
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, default=None)
    path = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_main = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"image path: {self.path}"
