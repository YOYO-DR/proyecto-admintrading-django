from django.urls import path
from .views import *

urlpatterns = [
  path('',principal,name="principal"),
  path('iniciarsesion/',iniciarsesion,name="iniciarsesion"),
  path('registro/',registro,name="registro"),
  path('cerrarsesion/',cerrarsesion,name="cerrar"),
]
