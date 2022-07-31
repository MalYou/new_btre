import uuid
from django.db import models

from listings.models import Listing


class Attachment(models.Model):
    """
        Manages attachment objects
    """

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, default=None, related_name="attachments")
    path = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_main = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"image path: {self.path}"
