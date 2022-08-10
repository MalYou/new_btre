import uuid
from django.db import models

from listings.models import Listing
from users.models import User


class Contact(models.Model):
    """
        Handle contact objects
    """

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    listing = models.ForeignKey(Listing, default=None, on_delete=models.DO_NOTHING, related_name="contacts")
    message = models.TextField(max_length=256, blank=True)
    customer = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING, related_name="contacts")
