from rest_framework import routers

from .views import ContactsViewSet

router = routers.DefaultRouter()
router.register(r"", ContactsViewSet, basename="contacts")

urlpatterns = router.urls
