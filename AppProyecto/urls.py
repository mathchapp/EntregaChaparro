from django.urls import path
from AppProyecto.views import *

urlpatterns = [
path('equipos/', equipo, name = "equipo"),
path('inicio/', inicio, name = "inicio"),
path('jugadores/', jugadores, name = "jugadores"),
path('ligas/', ligas, name = "ligas"),
path('buscarEquipos/', buscar),
path('formJug/', formularioJ),
path('formEquipo/', formularioE),
path('formLiga/', formularioL),
]