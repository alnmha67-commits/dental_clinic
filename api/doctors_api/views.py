from rest_framework.decorators import api_view
from rest_framework.response import Response
from.serializers import Doctors_Serializers
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from my_project.models import Doctor
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from .permission import Doctor_permission


class Api_Doctor(ModelViewSet):
  queryset=Doctor.objects.all()
  serializer_class=Doctors_Serializers
  permission_classes=[Doctor_permission]
  throttle_scope="doctor"
