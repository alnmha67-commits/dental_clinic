from rest_framework.test import APITestCase
from rest_framework import status
from api.appointment_api.serializers import Appointment_Serializers
from django.contrib.auth.models import User
from my_project.models import Patient,Doctor


class Test_Appointment_serializer(APITestCase):
    def setUp(self):
            self.doc_user = User.objects.create_user(username="dr_ahmed", password="password123")
            self.pat_user = User.objects.create_user(username="patient_ali", password="password123")
            self.admin_user = User.objects.create_user(username="poop",password="99",is_staff=True)
            
            
            self.doctor = Doctor.objects.create(
                user=self.doc_user,
                job="Dentist",
                discription="Dental Specialist"
            )
            
            
            self.patient = Patient.objects.create(
                user=self.pat_user,
                phone="0791234567",
                date_of_birth="1995-05-12"
            )
    def test_valid_time(self):
        appointment= {
                "patient":self.patient.id,
                "doctor":self.doctor.id,
                "start_appointment":"11:00:00",
                "end_appointment":"11:30:00",
                "date":"2026-11-10",
                "day":"Tuesday",
                "reson":"Checkup",
                "status":"pending"
            }
        serializer=Appointment_Serializers(data=appointment)
        self.assertTrue(serializer.is_valid())