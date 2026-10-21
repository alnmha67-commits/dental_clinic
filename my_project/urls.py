from django.urls import path
from . import views
urlpatterns=[
    path('main_page',views.main_page,name="main_page"),
    path('login_page',views.login_page,name="login_page"),
    path('first_login/',views.first_login,name="first_login"),
    path('doctor_page',views.doctor_page,name="doctor_page"),
    path('doctor_work/<int:doctor_id>',views.doctor_work,name="doctor_work"),
    path('profial_patient',views.profial_patient,name="profial_patient"),
    path('check_appointment/<int:doctor_id>/<str:start>/<str:end>/<str:day>/<str:date>',views.check_appointment,name="check_appointment"),
    path('pest',views.pest,name="pest"),
    path("add_appointment/<int:doctor_id>/<str:start>/<str:end>/<str:day>/<str:date>",views.add_appointment,name="add_appointment"),
    path('patient_login',views.patient_login,name="patient_login"),
    path('logut',views.logut,name="logut"),
    path('logut_page',views.logut_page,name="logut_page"),
    path('update_patient/<int:id>',views.update_patient,name="update_patient"),
    path('update_doctor/<int:id>',views.update_doctor,name="update_doctor"),
    path('update_img/<int:id>',views.update_img,name="update_img"),
    path('my_appointment',views.my_appointment,name="my_appointment"),
]