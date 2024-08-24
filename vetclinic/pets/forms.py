from django import forms
from .models import Owner, Pet, Consultation
from django.contrib.admin import widgets

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['identification', 'name', 'address', 'phone', 'email']
        labels = {
            'identification': ('Identificación'),
            'name': ('Nombre'),
            'address': ('Dirección'),
            'phone': ('Telefono'),
            'email': ('Correo electrónico'),
        }

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'age', 'owner', 'photo']
        labels = {
            'name': ('Nombre'),
            'species': ('Especie'),
            'breed': ('Raza'),
            'age': ('Edad'),
            'owner': ('Dueño'),
            'photo': ('Foto'),
        }

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['pet', 'date', 'description']
        labels = {
            'pet': ('Nombre Mascota'),
            'date': ('Fecha/Hora'),
            'description': ('Descripción'),
        }   