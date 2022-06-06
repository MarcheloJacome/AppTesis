from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.app_patient.models import Patient

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
    (0, _('Single Model')),
    (1, _('Ensemble Models')),
]

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
