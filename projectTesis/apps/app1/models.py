from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

sextype = [
    ('F', _('Female')),
    ('M', _('Male')),
]

cpt = [
    ('ASY', _('Asymptomatic')),
    ('ATA', _('Atypical Angina')),
    ('NAP', _('Non-Anginal Pain')),
    ('TA', _('Typical Angina')),
]

recg = [
    ('LVH', 'LVH'),
    ('Normal', 'Normal'),
    ('ST', 'ST'),
]

sts = [
    ('Down', _('DOWN')),
    ('Flat', _('FLAT')),
    ('Up', _('UP')),
]

fbs = [
    (0, _('Blood sugar <= 120 mg/dl')),
    (1, _('Blood sugar > 120 mg/dl')),
]

ea = [
    ('N', 'No'),
    ('Y', _('Yes')),
]

#heartdisease
hd = [
    (0, 'No'),
    (1, _('Yes')),
]
#aimodel
aimod = [
    (0, _('Single Model (XGB Classifier)')),
    (1, _('Soft Voting Ensemble Models')),
]




class Patient(models.Model):
    date_created = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id_number = models.CharField(max_length=15)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=1)
    last_prediction = models.IntegerField(null=True, choices=hd)
    last_prediction_prob = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.first_name +' '+self.last_name)
    def get_last_prediction(self):
        return self.prediction_set.last()

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



class PredictionToTrain(models.Model):
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
    aiModel = models.IntegerField(choices=aimod,max_length=50, null=True)
    prediction = models.OneToOneField(Prediction, on_delete=models.CASCADE, null = True)
    was_used = models.BooleanField(null = True)
    def __str__(self):
        return str(self.pk)