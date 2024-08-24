from django.shortcuts import render, redirect, get_object_or_404
from .models import Owner, Pet, Consultation
from .forms import OwnerForm, PetForm, ConsultationForm

def home(request):
    return render(request, 'home.html')

def owner_list(request):
    owners = Owner.objects.all()
    return render(request, 'owner_list.html', {'owners': owners})

def owner_create(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('owner_list')
    else:
        form = OwnerForm()
    return render(request, 'add_owner.html', {'form': form})

def owner_update(request, pk):
    owner = get_object_or_404(Owner, pk=pk)
    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_list')
    else:
        form = OwnerForm(instance=owner)
    return render(request, 'add_owner.html', {'form': form})

def pet_list(request):
    pets = Pet.objects.all()  
    return render(request, 'pet_list.html', {'pets': pets})


def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm()
    return render(request, 'add_pet.html', {'form': form})

def pet_update(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm(instance=pet)
    return render(request, 'add_pet.html', {'form': form})

def consultation_list(request):
    consultations = Consultation.objects.all()
    return render(request, 'consultation_list.html', {'consultations': consultations})



def consultation_create(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultation_list')
    else:
        form = ConsultationForm()
    return render(request, 'add_consultation.html', {'form': form})

def consultation_update(request, pk):
    consultation = get_object_or_404(Consultation, pk=pk)
    if request.method == 'POST':
        form = ConsultationForm(request.POST, instance=consultation)
        if form.is_valid():
            form.save()
            return redirect('consultation_list')
    else:
        form = ConsultationForm(instance=consultation)
    return render(request, 'add_consultation.html', {'form': form})
