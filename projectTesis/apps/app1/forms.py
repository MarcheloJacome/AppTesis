from django import forms
from django.forms import fields, widgets
from .models import Prediction
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PredictionForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields=['age','sex','chestPainType','restingBP','cholesterol','fastingBS','restingECG','maxHR','exerciseAngina','oldpeak','sT_Slope']
        labels = {
            'age':'Age of the patient (years)',
            'sex':'sex of the patient (M: Male, F: Female)',
            'chestPainType':'Chest pain type',
            'restingBP':'Resting blood pressure (mm/Hg)',
            'cholesterol':'Serum cholesterol (mm/dl)',
            'fastingBS':'Fasting blood sugar (1: if FastingBS > 120 mg/dl, 0: otherwise)',
            'restingECG':'Resting electrocardiogram results',
            'maxHR':'Maximum heart rate achieved',
            'exerciseAngina':'Exercise-induced angina (Y: Yes, N: No)',
            'oldpeak':'ST (Numeric value measured in depression)',
            'sT_Slope':'The slope of the peak exercise ST segment',
        }

