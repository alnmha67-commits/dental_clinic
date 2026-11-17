from django.conf import settings

from google.oauth2 import id_token
from google.auth.transport import requests as google_requests

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


@api_view(["POST"])
@permission_classes([AllowAny])
def google_login(request):
    token = request.data.get("id_token")

    if not token:
        return Response(
            {"error": "id_token is required"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        google_user = id_token.verify_oauth2_token(
            token,
            google_requests.Request(),
            settings.GOOGLE_CLIENT_ID,
        )
    except ValueError:
        return Response(
            {"error": "Invalid Google ID token"},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    return Response({
        "message": "Google token verified",
        "google_id": google_user["sub"],
        "email": google_user.get("email"),
    })