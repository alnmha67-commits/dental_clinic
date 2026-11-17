from rest_framework.response import Response
from.serializers import Patient_Serializers
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from my_project.models import Patient
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from .permission import Patient_permission
from ..pagination import Pagination_Api

class Api_Patient(ModelViewSet):
  queryset=Patient.objects.all()
  serializer_class=Patient_Serializers
  permission_classes=[Patient_permission]
  pagination_class=Pagination_Api
  def get_queryset(self):
    return Patient.object.filter(user=self.request.user)