from django.shortcuts import render, redirect, get_object_or_404
from .models import Owner, Pet, Consultation
from .forms import OwnerForm, PetForm, ConsultationForm

def home(request):
    return render(request, 'home.html')

def owner_list(request):
    owners = Owner.objects.all()
    return render(request, 'owner_list.html', {'owners': owners})

def owner_detail(request, pk):
    owner = get_object_or_404(Owner, pk=pk)
    return render(request, 'owner_detail.html', {'owner': owner})

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
    pets = Pet.objects.filter(owner=request.user)  # Adjust according to your user model
    return render(request, 'pet_list.html', {'pets': pets})

def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pet_detail.html', {'pet': pet})

def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm()
    return render(request, 'add_pet.html', {'form': form})

def pet_update(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm(instance=pet)
    return render(request, 'pet_form.html', {'form': form})

def consultation_detail(request, pk):
    consultation = get_object_or_404(Consultation, pk=pk)
    return render(request, 'consultation_detail.html', {'consultation': consultation})

def consultation_create(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultation_detail', pk=form.instance.pk)
    else:
        form = ConsultationForm()
    return render(request, 'add_consultation.html', {'form': form})

def consultation_update(request, pk):
    consultation = get_object_or_404(Consultation, pk=pk)
    if request.method == 'POST':
        form = ConsultationForm(request.POST, instance=consultation)
        if form.is_valid():
            form.save()
            return redirect('consultation_detail', pk=consultation.pk)
    else:
        form = ConsultationForm(instance=consultation)
    return render(request, 'pets/consultation_form.html', {'form': form})
