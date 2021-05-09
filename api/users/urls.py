from django.urls import path

from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='create'),
    path('me/', views.UserRetreiveView.as_view(), name='me'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='refresh_token'),
]
