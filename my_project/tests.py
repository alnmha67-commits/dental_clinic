from django.test import TestCase
from.services import check_patent,check_appointmente,add_appointmente,appointmentteked
from django.utils.dateparse import parse_date,parse_time
from.services import patent_not_found,patent_log



class TestAppointment(TestCase):
    def setUp(self):
        starte="01:00:00"
        endee="02:00:00"
        datee="2026-10-8"
        self.start=parse_time(starte)
        self.end=parse_time(endee)
        self.date=parse_date(datee)
        self.day="monday"
        self.user_id=9
        self.doctor_id=9

    def test_check_appointmente(self):
        with self.assertRaises(patent_not_found):
         check_appointmente(self.doctor_id,self.start,self.end,self.day,self.date,self.user_id)
    def test_check_appointment_whith_patient(self):
       patent_log(self.user_id,phone=1231231231,date="2000-01-10")
       result=check_appointmente(self.doctor_id,self.start,self.end,self.day,self.date,self.user_id)
       self.assertEqual(result,True)
        
        

