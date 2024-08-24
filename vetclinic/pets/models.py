from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Owner(models.Model):
    identification = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} ({self.identification})"

class Pet(models.Model):
    owner = models.ForeignKey(Owner, related_name='pets', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    photo = models.ImageField(upload_to='pets_photos/', blank=True, null=True)

    def __str__(self):
        return self.name

class Consultation(models.Model):
    pet = models.ForeignKey(Pet, related_name='consultations', on_delete=models.CASCADE)
    date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return f"Consulta para {self.pet.name} el {self.date.strftime('%Y-%m-%d')}"
