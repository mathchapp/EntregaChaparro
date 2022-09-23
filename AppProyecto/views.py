from django.shortcuts import render
from AppProyecto.models import Familiares, Liga, Jugador, Equipo
from django.http import HttpResponse
from AppProyecto.forms import FormularioEquipo, FormularioJugador, FormularioLiga
# Create your views here.


def inicio(request):

    return render(request, "AppProyecto/inicio.html")

def equipo(request):

    return render(request, "AppProyecto/equipos.html")

def jugadores(request):

    return render(request, "AppProyecto/jugadores.html")

def ligas(request):
    
    return render(request, "AppProyecto/ligas.html")


def formularioJ(request):

    if request.method=="POST":

      formularioJ = FormularioJugador(request.POST)

      if formularioJ.is_valid():  #Comprobar que no hayan errores

          info = formularioJ.cleaned_data
    
          jugadorF = Jugador(nombre=info["nombre"], apellido=info["apellido"], edad=info["edad"], puesto=info["puesto"]) #Lee la info de las cajas de texto

          jugadorF.save()

          return render(request, "AppProyecto/formularioJ.html")

    else:

      formularioJ = FormularioJugador()


    return render(request, "AppProyecto/formularioJ.html", {"formularioJ":formularioJ})

def formularioE(request):

    if request.method=="POST":

      formularioE = FormularioEquipo(request.POST)

      if formularioE.is_valid():  #Comprobar que no hayan errores

          info = formularioE.cleaned_data
    
          equipoF = Equipo(nombre=info["nombre"], procedencia=info["procedencia"], division=info["division"]) #Lee la info de las cajas de texto

          equipoF.save()

          return render(request, "AppProyecto/formularioE.html")

    else:

       formularioE = FormularioEquipo()


    return render(request, "AppProyecto/formularioE.html", {"formularioE":formularioE})



def formularioL(request):

    if request.method=="POST":

      formularioL = FormularioLiga(request.POST)

      if formularioL.is_valid():  #Comprobar que no hayan errores

          info = formularioL.cleaned_data
    
          ligaF = Liga(nombre=info["nombre"], pais=info["pais"], division=info["division"]) #Lee la info de las cajas de texto

          ligaF.save()

          return render(request, "AppProyecto/formularioL.html")

    else:

       formularioL = FormularioLiga()


    return render(request, "AppProyecto/formularioL.html", {"formularioL":formularioL})

def buscadorEquipos(request):
  return render(request, "AppProyecto/buscadorEquipos.html")  

def buscar(request):
    if request.GET["nombre"]:

        equipo = request.GET["nombre"]
        equipos = Equipo.objects.filter(nombre__icontains=nombre)

        return render(request, "AppProyecto/buscarEquipos.html", {"equipos":equipos, "equipo":equipo})

    else:

        mensaje = "No enviaste datos."
    return HttpResponse(mensaje)


























"""
def Familia(request):
    familiar = Familiares(nombre ="Mathias", edad =30, fechaNac =("1991-12-25"))
   
    familiar.save()
   
    documentoDeTexto = f"Mi nombre es {familiar.nombre}, tengo {familiar.edad} años de edad y mi fecha de nacimiento es el {familiar.fechaNac}"

    return HttpResponse(documentoDeTexto)

def template(self):
    
    planilla = loader.get_template("template.html")

    documento = planilla.render()

    return HttpResponse(documento)
"""