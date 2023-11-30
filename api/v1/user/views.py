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

    def partial_update(self, request, pk=None):
        serializer = UpdateUserInfoSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data=data, status=status.HTTP_202_ACCEPTED)