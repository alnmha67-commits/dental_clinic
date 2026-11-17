from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from.models import Doctor,Patient,Doctor_work,Appointment
from datetime import datetime,timedelta
from django.utils.dateparse import parse_date,parse_time
from .services import doctor_worke,my_appointmente,update_doctore,patient_update,patent_log,profile,check_appointmente,add_appointmente,appointmentteked,patent_not_found,patent_exsist
from django.core.exceptions import ValidationError



def main_page(request):
    return render(request,'my_project/main_page.html')
def first_login(request):
    if request.method == "POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        passwor=request.POST.get("password")
        usere=User.objects.filter(username=username)
        if usere.exists():
            return JsonResponse({"masseg":"accont alredy axists"})
        else:
           user= User.objects.create_user(username=username,email=email,password=passwor)
           login(request,user)
           return redirect('patient_login')
    return render(request,'my_project/first_login.html')
def login_page(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("main_page")
        else:
            return JsonResponse({"masseg":"your accont not exists"})
    return render(request,"my_project/login_page.html")

def doctor_page(request):
    doctor=Doctor.objects.all()
    return render(request,'my_project/doctor_page.html',{"doctor":doctor})
@login_required
def doctor_work(request, doctor_id):
    schedules,doctor=doctor_worke(doctor_id=doctor_id)
    return render(request,"my_project/doctor_work.html",{"schedules": schedules,"doctor":doctor})
@login_required
def check_appointment(request,doctor_id,start,end,day,date):
        user_id=request.user.id
        try:
            check_appointmente(doctor_id,start,end,day,date,user_id)
            return redirect("add_appointment",doctor_id=doctor_id,start=start,end=end,day=day,date=date)
        except appointmentteked:
            return redirect("pest")
        except patent_not_found:
            return redirect("patient_login")
def pest(request):
    return render(request,'my_project/pest.html')
@login_required
def patient_login(request):
    if request.method=='POST':
        user_id=request.user.id
        date=request.POST.get('date')
        phone=request.POST.get('phone')
        try:
          patent_log(user_id=user_id,phone=phone,date=date)
          return redirect('main_page')
        except ValueError:
            return redirect("pest")
        except ValidationError:
            return JsonResponse({"massag":"error phone not"})
    return render(request,'my_project/patient_login.html')
@login_required
def add_appointment(request,doctor_id,start,end,day,date):
    user_id=request.user.id
    doctor=Doctor.objects.get(id=doctor_id)
    starte=parse_time(start)
    ende=parse_time(end)
    if request.method=='POST':
        reson=request.POST.get('reson')
        try:
           x=add_appointmente(doctor,start,end,day,date,user_id,reson)
        except appointmentteked:
            return redirect("pest")
        except patent_not_found:
            return redirect("patient_login")
        return redirect("my_appointment")
    return render(request,'my_project/add_appointment.html',{'doctor':doctor,'start':starte,'end':ende,'day':day})
@login_required
def profial_patient(request):
    user_id=request.user.id
    doctor,patient=profile(user_id)
    if doctor==None and patient==None:
           return redirect('patient_login')
    return render(request,'my_project/profial_patient.html',{'doctor':doctor,'patient':patient})
@login_required
def logut_page(request):
    return render(request,'my_project/logut_page.html')
@login_required
def logut(request):
    logout(request)
    return redirect('main_page')

def update_patient(request,id):
    patient=Patient.objects.get(id=id)
    if request.method=="POST":
        phone=request.POST.get('phone')
        date=request.POST.get('date')
        patient_update(patient,date,phone)
        return redirect('profial_patient')
    return render (request,'my_project/update_patient.html',{'patient':patient})
def  update_doctor(request,id):
    doctor=Doctor.objects.get(id=id)
    if request.method=="POST":
        job=request.POST.get('job')
        discription=request.POST.get('discription')
        update_doctore(doctor,job,discription)
       
        return redirect("profial_patient",)
    return render(request,'my_project/update_doctor.html',{'doctor':doctor})
def update_img(request,id):
    doctor=Doctor.objects.get(id=id)
    if request.method=="POST":
        img=request.FILES.get("img")
        if img:
            doctor.img=img
            doctor.save()
            return redirect("profial_patient")
    return render(request,'my_project/update_img.html',{'doctor':doctor})
def my_appointment(request):
    user_id=request.user.id
    appointments=my_appointmente(user_id)
    return render(request,'my_project/my_appointment.html',{'appointments':appointments})
def google(request):
    return render (request,"my_project/google.html")