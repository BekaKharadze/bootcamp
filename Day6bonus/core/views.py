from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .permissions import IsAdminUserOrReadOnly
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": "You are logged in!"})

@api_view(['GET', 'POST'])
@permission_classes([IsAdminUserOrReadOnly])
def admin_only_view(request):
    return Response({"message": "Admins can modify, others can only read."})