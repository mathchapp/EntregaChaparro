from django import forms

class FormularioJugador(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    puesto = forms.CharField()

class FormularioEquipo(forms.Form):
    nombre = forms.CharField()
    procedencia = forms.CharField()
    division = forms.CharField()

class FormularioLiga(forms.Form):
    nombre = forms.CharField()
    pais = forms.CharField()
    division = forms.CharField()