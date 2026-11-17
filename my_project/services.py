from .models import Doctor,Doctor_work,Appointment,Patient
from datetime import datetime,timedelta
from django.utils.dateparse import parse_date,parse_time
from .exptions import appointmentteked,patent_not_found,patent_exsist
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db import transaction
import logging
from threading import Lock
from django.core.cache import cache
logger=logging.getLogger("my_project")
loks=Lock()
def doctor_worke(doctor_id):
    doctor_works=cache.get(f"docto_works_{doctor_id}")
    if doctor_works is None:
       with loks:
            doctor_works=cache.get(f"doctor_works_{doctor_id}")
            if doctor_works is None:
               doctor_works =Doctor_work.objects.select_related('doctor').filter(doctor_id=doctor_id)
            cache.set(f"doctor_works_{doctor_id}",doctor_works,timeout=10*60)  
    doctor=doctor_works[0].doctor
    schedules = []
    for work in doctor_works:
        current_time = datetime.combine(
            datetime.today(),
            work.start_work
        )
        end_time = datetime.combine(
            datetime.today(),
            work.end_work
        )
        slots = []
        while current_time < end_time:
            appointment_end = current_time + timedelta(minutes=30)
            if appointment_end <= end_time:
                slots.append({
                    "start": current_time.time(),
                   "end": appointment_end.time(),
                })
            current_time = appointment_end
        schedules.append({
            "date":work.date,
            "day": work.day,
            "slots": slots,
        })
        return schedules,doctor
def check_appointmente(doctor_id,start,end,day,date,user_id):
    logger.debug("check if appointment is booked for user=%s,doctor=%s",user_id,doctor_id)
    check_patent(user_id)
    starte=parse_time(start)
    ende=parse_time(end)
    datee=parse_date(date)
    x=Appointment.objects.filter(start_appointment=starte,doctor_id=doctor_id,day=day)
    print(x.explain(analyze=True,buffers=True))
    if x:
         m=x[0]
         logger.error("Appointment is booked Appointment=%s",m.id)
         raise appointmentteked("")
    else:
         logger.info("Appointment not taked")
         return True
def check_patent(user_id):
    logger.debug("check patient to user=%s",user_id)
    try:
          Patient.objects.get(user_id=user_id)
          logger.info("patient exsist")
          return True
    except Patient.DoesNotExist:
         logger.error("patient not exsist")
         raise patent_not_found("")

def add_appointmente(doctor,start,end,day,date,user_id,reson):
    logger.debug("add Appointment for doctor=%s,patent=%s,date=%s",doctor.id,user_id,date)
    check_patent(user_id)
    starte=parse_time(start)
    ende=parse_time(end)
    datee=parse_date(date)
    status='confirmed'
    patient=Patient.objects.get(user_id=user_id)
    try:
           Appointment.objects.create(start_appointment=starte,
                    end_appointment=ende,patient=patient,doctor=doctor,
                    day=day,reson=reson,status=status,date=datee)
           cache.delete("check_appointment")
    except IntegrityError:
           logger.error("appoinment taked")
           raise appointmentteked("")
    

    
def profile(user_id):
        try:
          doctor=Doctor.objects.get(user_id=user_id)
        except Doctor.DoesNotExist:
            doctor=None
        try:
             patient=Patient.objects.get(user_id=user_id)
        except Patient.DoesNotExist:
           patient=None
        return doctor,patient
def patent_log(user_id,date,phone):
    if len(phone)!=10:
         raise ValidationError("")
    try:
      patient=Patient(user_id=user_id,phone=phone,date_of_birth=date)
      patient.full_clean()
      patient.save()
    except IntegrityError:
        raise patent_exsist("")
    except ValidationError:
         raise ValueError("")
def patient_update(patient,date,phone):
    if date:
             patient.date_of_birth=date
             patient.save()
             if phone:
              patient.phone=phone
              patient.save()
def update_doctore(doctor,job,discription):
     if job :
                doctor.job=job
                doctor.save()
     if discription:
                doctor.discription=discription
                doctor.save()
def my_appointmente(user_id):
   patient=None
   doctor=None
   try:
     doctor=cache.get("doctor")
     if doctor is None:
          with loks:
               doctor=cache.get("doctor")
               if doctor is None:
                  doctor=list(Doctor.objects.prefetch_related('appointment').get(user_id=user_id))
                  cache.set("doctor",doctor,timeout=10*60)
     return doctor.appointment.all()
   except Doctor.DoesNotExist:
       doctor=None
       patient=Patient.objects.prefetch_related('appointment').get(user_id=user_id)
       return patient.appointment.all()

    
    

     




  


