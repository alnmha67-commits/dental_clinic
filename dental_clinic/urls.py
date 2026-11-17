"""
URL configuration for dental_clinic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dental/',include('my_project.urls')),
    path('api_doctor/',include('api.doctors_api.urls')),
    path('api_patient/',include('api.patient_api.urls')),
    path('api_doctor_work/',include('api.doctor_work_api.urls')),
    path('api_appointment/',include('api.appointment_api.urls')),
    path('api/auth/',include('api.accounts.urls')),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
handler500="my_project.handlers.custom_500"
handler400="my_project.handlers.custom_400"
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
