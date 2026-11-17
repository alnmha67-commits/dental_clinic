from rest_framework import serializers
from my_project.models import Doctor

class Doctors_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields="__all__"