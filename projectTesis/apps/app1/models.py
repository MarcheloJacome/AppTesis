from django.db import models

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


# Create your models here.
class Prediction(models.Model):
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
    heartDisease = models.BooleanField(null=True)
    def __str__(self):
        return str(self.pk)