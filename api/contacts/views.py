from rest_framework import viewsets, mixins
from rest_framework.settings import api_settings

from . import models
from . import serializers


class ContactsViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    """
        view to retrieve contacts objects
    """

    queryset = models.Contact
    serializer_class = serializers.ContactsSerializer
    lookup_field = "listing"
    authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
