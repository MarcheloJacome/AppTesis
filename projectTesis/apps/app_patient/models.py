from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

hd = [
    (0, 'No'),
    (1, _('Yes')),
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

