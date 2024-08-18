from django import forms
from .models import Owner, Pet, Consultation

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['identification', 'name', 'address', 'phone', 'email']

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'age', 'owner']

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['pet', 'date', 'description']
