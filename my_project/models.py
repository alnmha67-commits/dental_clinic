from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta,date
from django.utils.dateparse import parse_date,parse_time
from django.core.exceptions import ValidationError
class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    job=models.CharField(max_length=20)
    discription=models.CharField(max_length=50)
    img=models.ImageField(upload_to='doctors/')
    def __str__(self):
           return self.user.username

class Patient(models.Model):
    user=models.OneToOneField(User,db_index=True,on_delete=models.CASCADE)
    phone=models.CharField(max_length=15)
    date_of_birth=models.DateField()
    def clean(self):
         if len(self.phone)!=10:
              raise ValidationError("namber not 10 digit")
         date_patient=self.date_of_birth
         if date_patient> date.today()-timedelta(days=3652):
              raise ValidationError("your age is yang")
    def __str__(self):
         return self.user.username
class Doctor_work(models.Model):
     doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='doctor')
     day=models.CharField(max_length=10)
     start_work=models.TimeField()
     end_work=models.TimeField()
     date=models.DateField(null=True,blank=True)
     def clean(self):
          if self.start_work and self.end_work and self.start_work>=self.end_work:
               raise ValueError("start time not good for work")
          toda=date.today()
          if toda>self.date:
               raise ValidationError("")
     def __str__(self):
          return self.doctor.user.username
class Appointment(models.Model):
     start_appointment=models.TimeField()
     end_appointment=models.TimeField()
     patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='appointment')
     doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='appointment')
     date=models.DateField()
     day=models.CharField(max_length=10)
     reson=models.CharField(max_length=40)
     status=models.CharField(max_length=20)
     def clean(self):
          if self.start_appointment and self.end_appointment and self.start_appointment>=self.end_appointment:
               raise ValueError("this appointment not exsists ")
     class Meta:
          indexes=[models.Index(fields=['start_appointment','doctor','day'],name="aa")]
          constraints=[models.UniqueConstraint(fields=["doctor","day"
                         ,"start_appointment","end_appointment","date"]
                         ,name="unique_appointment")]





# Create your models here.
