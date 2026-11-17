from rest_framework import serializers
from my_project.models import Doctor_work

class Doctors_Work_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Doctor_work
        fields="__all__"