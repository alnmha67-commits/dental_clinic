from django.urls import path,include
from .views import Api_Patient
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
router=DefaultRouter()
router.register("",Api_Patient)
urlpatterns=[path('',include(router.urls)),
             path('api/token',TokenObtainPairView.as_view()),
             path('api/token/refresh',TokenRefreshView.as_view()),
             ]