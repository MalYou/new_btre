from rest_framework import viewsets
from rest_framework.settings import api_settings

from .models import Listing
from .serializers import ListingSerializer


class ListingViewSet(viewsets.ReadOnlyModelViewSet):
    """
        List listings or retrive a specific listing
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
