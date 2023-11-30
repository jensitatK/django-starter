from .models import User
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import UserSerializer, UpdateUserInfoSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
