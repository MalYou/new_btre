from django.db.models import Prefetch
from rest_framework import viewsets, mixins, permissions

from attachments.models import Attachment
from .models import Listing
from . import serializers


class ListingsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
        List listings or retrieve a specific listing
    """
    serializer_class = serializers.ListingsSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
         This view should retur a list of listings including only the genecis details
        """

        listings = Listing.objects.prefetch_related(
            Prefetch("attachments", queryset=Attachment.objects.filter(is_main=True))
        )

        return listings


class ListingViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
        List listings or retrieve a specific listing
    """

    queryset = Listing.objects.all()
    serializer_class = serializers.ListingSerializer
    permission_classes = [permissions.AllowAny]
