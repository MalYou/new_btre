from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.settings import api_settings

from .serializers import UserSerializer

class UserCreateView(generics.CreateAPIView):
    """ View for creating a new user """

    serializer_class = UserSerializer


class UserRetreiveView(generics.RetrieveAPIView):
    """ View for retreiving a connect user """

    serializer_class = UserSerializer
    authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES

    def get_object(self):
        """ Returns the connected user """
        return self.request.user
