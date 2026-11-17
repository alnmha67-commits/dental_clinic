from rest_framework.test import APITestCase
from rest_framework import status
from my_project.models import Appointment,Doctor,Patient
from django.contrib.auth.models import User

class Test_Appointment_Model(APITestCase):
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
    def test_appointment_create(self):
          u=User.objects.create(username="ppo",password="8878787")
          patientt=Patient.objects.create(user=u,
                          phone="0791234567",
                          date_of_birth="1995-05-12")
          appointment=Appointment.objects.create(
                patient=patientt,
                doctor=self.doctor,
                start_appointment="11:00:00",
                end_appointment="11:30:00",
                date="2026-11-10",
                day="Tuesday",
                reson="Checkup",
                status="pending"
          )
          self.assertEqual(appointment.day,"Tuesday")
          self.assertEqual(Appointment.objects.count(),1)
          self.assertEqual(appointment.patient,patientt)
          patientt.delete()
          self.assertFalse(Appointment.objects.filter(id=appointment.id).exists())

