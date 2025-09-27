from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_patient=models.BooleanField(default=False)
    is_doctor=models.BooleanField(default=False)



class Patient(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name="patient")
    Patient_name=models.CharField(max_length=25)
    Patient_email=models.EmailField()
    Patient_phone_no=models.CharField(max_length=10)
    blood_choices = (
        ("A+", "A+" ),
        ("B+","B+"),
        ("O+","O+"),
        ("AB+","AB+"),
        ("A-","A-"),
        ("B-","B-"),
        ("O-","O-"),
        ("AB-","AB-")

    )
    Patient_blood_group=models.CharField(max_length=5,choices=blood_choices)

    def __str__(self):
        return self.Patient_name

class Department(models.Model):
    Department_name=models.CharField(max_length=20)
    Department_phone_no=models.CharField(max_length=10)
    Department_email=models.EmailField()
    Department_image=models.FileField(upload_to ='Department_image/')

    def __str__(self):
        return self.Department_name


class Doctor(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name="doctor")
    Doctor_name=models.CharField(max_length=20)
    Doctor_Department=models.ForeignKey("Department",on_delete=models.DO_NOTHING)
    Doctor_phone_no=models.CharField(max_length=10)
    Doctor_email=models.EmailField()

    def __str__(self):
        return self.Doctor_name