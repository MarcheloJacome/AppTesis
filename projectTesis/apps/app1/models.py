from django.db import models
from django.contrib.auth.models import User
sextype = [
    ('F', 'Female'),
    ('M', 'Male'),
]

cpt = [
    ('ASY', 'Asymptomatic'),
    ('ATA', 'Atypical Angina'),
    ('NAP', 'Non-Anginal Pain'),
    ('TA', 'Typical Angina'),
]

recg = [
    ('LVH', 'LVH'),
    ('Normal', 'Normal'),
    ('ST', 'ST'),
]

sts = [
    ('Down', 'DOWN'),
    ('Flat', 'FLAT'),
    ('Up', 'UP'),
]

fbs = [
    (0, 'Otherwise'),
    (1, 'FastingBS > 120 mg/dl'),
]

ea = [
    ('N', 'No'),
    ('Y', 'Yes'),
]

#heartdisease
hd = [
    (0, 'No'),
    (1, 'Yes'),
]
#aimodel
aimod = [
    (0, 'Single Model (K-Nearest Neighbors)'),
    (1, 'Hard Voting Ensemble Models'),
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
    sex = models.CharField(choices=sextype,max_length=10)
    chestPainType = models.CharField(choices=cpt,max_length=10)
    restingBP = models.PositiveIntegerField()
    cholesterol = models.PositiveIntegerField()
    fastingBS = models.IntegerField(choices=fbs)
    restingECG = models.CharField(choices=recg,max_length=10)
    maxHR = models.PositiveIntegerField()
    exerciseAngina = models.CharField(choices=ea,max_length=10)
    oldpeak = models.DecimalField(max_digits=5, decimal_places=2)
    sT_Slope = models.CharField(choices=sts,max_length=10)
    heartDisease = models.IntegerField(null=True, choices=hd)
    heartDiseaseProb = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    aiModel = models.IntegerField(choices=aimod,max_length=50, null=True)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null = True)
    def __str__(self):
        return str(self.pk)