from django.db import models
import uuid
from django.core.validators import RegexValidator
from django.utils.timezone import now

class Donor(models.Model):
    donor_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    donor_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone_validator = RegexValidator(regex=r'^\+?\d{10,15}$', message="Enter a valid phone number.")
    phone_no = models.CharField(max_length=15, validators=[phone_validator])
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=50, db_index=True)
    address = models.TextField()
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')
    ]
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, db_index=True)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return f"{self.donor_name} ({self.blood_group})"

class Request(models.Model):
    pat_name = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    units = models.PositiveIntegerField()
    pat_id = models.CharField(max_length=50, unique=True, editable=False, default=uuid.uuid4)
    def __str__(self):
        return self.pat_name

class BloodInventory(models.Model):
    blood_type = models.CharField(max_length=10, unique=True)
    units = models.PositiveIntegerField()

    def __str__(self):
        return self.blood_type
