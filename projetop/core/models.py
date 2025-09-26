from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_psychologist = models.BooleanField(default=False)
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)

class PsychologistProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    crp = models.CharField(max_length=20, unique=True)
    bio = models.TextField(blank=True, null=True)
    especialidades = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} - {self.crp}"

class Appointment(models.Model):
    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("confirmada", "Confirmada"),
        ("concluída", "Concluída"),
        ("cancelada", "Cancelada"),
    ]
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments_as_patient")
    psychologist = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments_as_psychologist")
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pendente")

    def __str__(self):
        return f"{self.date} - {self.patient} com {self.psychologist}"
