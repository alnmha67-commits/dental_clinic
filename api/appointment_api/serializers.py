from rest_framework import serializers
from my_project.models import Appointment

class Appointment_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields="__all__"
