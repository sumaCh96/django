
from django.urls import path,include
from rest_framework import routers

from .views import EmployeeCurd, login

router = routers.DefaultRouter()

router.register(r"rout",EmployeeCurd,basename="rout")


urlpatterns = [
    path('',include(router.urls)),
    path('api/login', login),

]