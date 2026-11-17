from.serializers import Appointment_Serializers
from rest_framework.viewsets import ModelViewSet
from my_project.models import Doctor_work
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from .permission import Appointment_permission
from my_project.models import Appointment
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from django.core.cache import cache
from threading import Lock
loks=Lock()

class Api_Appointment(ModelViewSet):
  queryset=Appointment.objects.all()
  serializer_class=Appointment_Serializers
  permission_classes=[Appointment_permission]
  filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
  search_fields=["doctor","patient","start_appointment"]
  filterset_fields=["doctor","start_appointment"]
  throttle_scope='appointment'

  
  def get_queryset(self):
     queryset=cache.get("appointment")
     if queryset is None:
          with loks:
             queryset=cache.get("appointment")
             if queryset is None:
              appointment=Appointment.objects.all()
              cache.set("appointment",appointment,timeout=5*60)
    
     x=self.request.query_params.get("appointment")
     if x:
      queryset=Appointment.objects.filter(status=x)
     return queryset
  def perform_create(self, serializer):
    serializer.save()
    cache.delete("appointment")
  def perform_destroy(self, instance):
    instance.delete()
    cache.delete("appointment")
  def perform_update(self, serializer):
    serializer.save()
    cache.delete("appointment")