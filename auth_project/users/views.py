# users/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny  # Add this import
from django.contrib.auth.models import User
from .serializers import RegisterSerializer


# View for user registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]  # Ensure this line is present
    serializer_class = RegisterSerializer


# View for user profile (protected route)
class UserProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        })
