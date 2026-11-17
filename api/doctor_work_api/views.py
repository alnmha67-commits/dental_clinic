from.serializers import Doctors_Work_Serializers
from rest_framework.viewsets import ModelViewSet
from my_project.models import Doctor_work
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from .permission import Doctor_Work_permission


class Api_Doctor_Work(ModelViewSet):
  queryset=Doctor_work.objects.all()
  serializer_class=Doctors_Work_Serializers
  permission_classes=[Doctor_Work_permission]