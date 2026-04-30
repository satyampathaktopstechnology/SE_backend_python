from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # owner (doctor/user)

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    condition = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    STATUS_CHOICES = [
        ("upcoming", "Upcoming"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    date = models.DateField()
    time = models.TimeField()

    doctor = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="upcoming")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} - {self.date}"