from rest_framework import serializers
from my_project.models import Patient

class Patient_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields="__all__"