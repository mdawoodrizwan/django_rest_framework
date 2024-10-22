# users/urls.py
from django.urls import path
from .views import RegisterView, UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT Token endpoint
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token refresh endpoint
    path('profile/', UserProfileView.as_view(), name='profile'),  # Protected profile endpoint
]
