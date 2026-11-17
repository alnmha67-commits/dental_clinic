from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from my_project.models import Patient,Doctor

from datetime import date
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from my_project.models import Doctor, Patient, Appointment # (استبدل my_project باسم التطبيق لديك)

class Test_Appointment(APITestCase):
    
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
        
    
        self.appointment = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            start_appointment="10:00:00",
            end_appointment="10:30:00",
            date="2026-11-10",
            day="Tuesday",
            reson="Checkup",
            status="pending"
        )

    def test_get_appointment(self):
        response = self.client.get("/api_appointment/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_post_appointment(self):
        self.client.force_authenticate(user=self.admin_user)
        appointment = {
            "patient":self.patient.id,
            "doctor":self.doctor.id,
            "start_appointment":"11:00:00",
            "end_appointment":"11:30:00",
            "date":"2026-11-10",
            "day":"Tuesday",
            "reson":"Checkup",
            "status":"pending"
        }
        response=self.client.post("/api_appointment/",appointment)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        
      