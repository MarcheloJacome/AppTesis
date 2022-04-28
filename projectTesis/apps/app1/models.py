from django.db import models
from django.contrib.auth.models import User
sextype = [
    (0, 'Female'),
    (1, 'Male'),
]

cpt = [
    (0, 'Asymptomatic'),
    (1, 'Atypical Angina'),
    (2, 'Non-Anginal Pain'),
    (3, 'Typical Angina'),
]

recg = [
    (0, 'LVH'),
    (1, 'Normal'),
    (2, 'ST'),
]

sts = [
    (0, 'DOWN'),
    (1, 'FLAT'),
    (2, 'UP'),
]

fbs = [
    (0, 'Otherwise'),
    (1, 'FastingBS > 120 mg/dl'),
]

ea = [
    (0, 'No'),
    (1, 'Yes'),
]

#heartdisease
hd = [
    (0, 'No'),
    (1, 'Yes'),
]


class Physician(models.Model):
    date_created = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id_number = models.CharField(max_length=15)
    sex = models.IntegerField(choices=sextype)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30)
    specialty = models.CharField(max_length=100)
    def __str__(self):
        return str(self.first_name +' '+self.last_name)

class Patient(models.Model):
    date_created = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id_number = models.CharField(max_length=15)
    #sex = models.IntegerField(choices=sextype)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30)
    #age = models.PositiveIntegerField()
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    #physician = models.ForeignKey(Physician, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.first_name +' '+self.last_name)

# Create your models here.
class Prediction(models.Model):
    date_created = models.DateField(null = True)
    age = models.PositiveIntegerField()
    sex = models.IntegerField(choices=sextype)
    chestPainType = models.IntegerField(choices=cpt)
    restingBP = models.PositiveIntegerField()
    cholesterol = models.PositiveIntegerField()
    fastingBS = models.IntegerField(choices=fbs)
    restingECG = models.IntegerField(choices=recg)
    maxHR = models.PositiveIntegerField()
    exerciseAngina = models.IntegerField(choices=ea)
    oldpeak = models.DecimalField(max_digits=5, decimal_places=2)
    sT_Slope = models.IntegerField(choices=sts)
    heartDisease = models.IntegerField(null=True, choices=hd)
    heartDiseaseProb = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null = True)
    def __str__(self):
        return str(self.pk)