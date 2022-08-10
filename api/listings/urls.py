from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"", viewset=views.ListingsViewSet, basename="listings")
router.register(r"", viewset=views.ListingViewSet, basename="listing-details")

urlpatterns = router.urls
