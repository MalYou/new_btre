from django.urls import path

from rest_framework_simplejwt import views as views

from .views import UserView

urlpatterns = [
    path('', UserView.as_view(), name='users'), 
    path('token/', views.TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', views.TokenRefreshView.as_view(), name='refresh_token'),
]