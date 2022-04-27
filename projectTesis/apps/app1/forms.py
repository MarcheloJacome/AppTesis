from django import forms
from django.forms import fields, widgets
from .models import Patient, Prediction
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'password1', 'password2')

class EditUserForm(UserChangeForm):
    #def __init__(self, *args, **kwargs):
    #    super(EditUserForm, self).__init__(*args, **kwargs)
    #    for visible in self.visible_fields():
    #        visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

#class CustomPasswordChangeForm(PasswordChangeForm):
    #def __init__(self, *args, **kwargs):
    #    super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
    #    for visible in self.visible_fields():
    #        visible.field.widget.attrs['class'] = 'form-control'  
      
class CreatePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'first_name',
            'last_name',
            'id_number',
            'sex',
            'city',
            'address',
            'phone_number',
            'age',
            'height',
            'weight',
        ]
        labels = {
            'first_name':'First Name',
            'last_name':'Last Name',
            'id_number':'ID Number',
            'sex':'Sex',
            'city':'City',
            'address':'Adress',
            'phone_number':'Phone Number',
            'age':'Age',
            'height':'Height',
            'weight':'Weigth',
        }

class DetailPatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(DetailPatientForm, self).__init__(*args, **kwargs)
       self.fields['first_name'].widget.attrs['readonly'] = True
       self.fields['last_name'].widget.attrs['readonly'] = True
       self.fields['id_number'].widget.attrs['readonly'] = True
      # self.fields['sex'].widget.attrs['readonly'] = True
       self.fields['sex'].widget.attrs['disabled'] = True
       self.fields['city'].widget.attrs['readonly'] = True
       self.fields['address'].widget.attrs['readonly'] = True
       self.fields['phone_number'].widget.attrs['readonly'] = True
       self.fields['age'].widget.attrs['readonly'] = True
       self.fields['height'].widget.attrs['readonly'] = True
       self.fields['weight'].widget.attrs['readonly'] = True
    class Meta:
        model = Patient
        fields = [
            'first_name',
            'last_name',
            'id_number',
            'sex',
            'city',
            'address',
            'phone_number',
            'age',
            'height',
            'weight',
        ]
        labels = {
            'first_name':'First Name',
            'last_name':'Last Name',
            'id_number':'ID Number',
            'sex':'Sex',
            'city':'City',
            'address':'Adress',
            'phone_number':'Phone Number',
            'age':'Age',
            'height':'Height (cm)',
            'weight':'Weigth (kg)',
        }

class MakePredictionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(MakePredictionForm, self).__init__(*args, **kwargs)
       self.fields['heartDisease'].widget.attrs['disabled'] = True
       self.fields['heartDisease'].required = False
    class Meta:
        model = Prediction
        fields=['date_created','age','sex','chestPainType','restingBP','cholesterol','fastingBS','restingECG','maxHR','exerciseAngina','oldpeak','sT_Slope','heartDisease']
        labels = {
            'date_created':'Date',
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
            'heartDisease':'Heart Disease',
        }
        widgets = {
            'date_created': DateInput,
        }

class DetailPredictionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(DetailPredictionForm, self).__init__(*args, **kwargs)
       self.fields['date_created'].widget.attrs['readonly'] = True
       self.fields['age'].widget.attrs['readonly'] = True
       self.fields['sex'].widget.attrs['disabled'] = True
       self.fields['chestPainType'].widget.attrs['disabled'] = True
       self.fields['restingBP'].widget.attrs['disabled'] = True
      # self.fields['sex'].widget.attrs['readonly'] = True
       self.fields['cholesterol'].widget.attrs['readonly'] = True
       self.fields['fastingBS'].widget.attrs['disabled'] = True
       self.fields['restingECG'].widget.attrs['disabled'] = True
       self.fields['maxHR'].widget.attrs['readonly'] = True
       self.fields['exerciseAngina'].widget.attrs['disabled'] = True
       self.fields['oldpeak'].widget.attrs['readonly'] = True
       self.fields['sT_Slope'].widget.attrs['disabled'] = True
       self.fields['heartDisease'].widget.attrs['disabled'] = True
    class Meta:
        model = Prediction
        fields=['date_created','age','sex','chestPainType','restingBP','cholesterol','fastingBS','restingECG','maxHR','exerciseAngina','oldpeak','sT_Slope','heartDisease']
        labels = {
            'date_created':'Creation date',
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
            'heartDisease':'Heart Disease',
        }

class PredictionForm(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
    #    super(PredictionForm, self).__init__(*args, **kwargs)
    #    for visible in self.visible_fields():
    #        visible.field.widget.attrs['class'] = 'form-control'
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

