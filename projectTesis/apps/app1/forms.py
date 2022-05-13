from random import choices
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
            #'sex',
            'city',
            'address',
            'phone_number',
            #'age',
            'height',
            'weight',
        ]
        labels = {
            'first_name':'First Name',
            'last_name':'Last Name',
            'id_number':'ID Number',
            #'sex':'Sex',
            'city':'City',
            'address':'Adress',
            'phone_number':'Phone Number',
            #'age':'Age',
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
       #self.fields['sex'].widget.attrs['disabled'] = True
       self.fields['city'].widget.attrs['readonly'] = True
       self.fields['address'].widget.attrs['readonly'] = True
       self.fields['phone_number'].widget.attrs['readonly'] = True
       #self.fields['age'].widget.attrs['readonly'] = True
       self.fields['height'].widget.attrs['readonly'] = True
       self.fields['weight'].widget.attrs['readonly'] = True
    class Meta:
        model = Patient
        fields = [
            'first_name',
            'last_name',
            'id_number',
            #'sex',
            'city',
            'address',
            'phone_number',
            #'age',
            'height',
            'weight',
        ]
        labels = {
            'first_name':'First Name',
            'last_name':'Last Name',
            'id_number':'ID Number',
            #'sex':'Sex',
            'city':'City',
            'address':'Adress',
            'phone_number':'Phone Number',
            #'age':'Age',
            'height':'Height (cm)',
            'weight':'Weigth (kg)',
        }



    

class MakePredictionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(MakePredictionForm, self).__init__(*args, **kwargs)
       self.fields['heartDisease'].widget.attrs['disabled'] = True
       self.fields['heartDisease'].required = False
       self.fields['heartDiseaseProb'].widget.attrs['disabled'] = True
       self.fields['heartDiseaseProb'].required = False
        #Fields Description
       self.fields['age'].widget.attrs['title'] = 'Age of the patient in years'
       self.fields['sex'].widget.attrs['title'] = 'Sex of the patient'
       self.fields['chestPainType'].widget.attrs['title'] = 'Type of chest pain'
       self.fields['restingBP'].widget.attrs['title'] = 'Resting blood pressure measured in: mm/Hg'
       self.fields['cholesterol'].widget.attrs['title'] = 'Serum cholesterol measured in mm/dl'
       self.fields['fastingBS'].widget.attrs['title'] = 'Fasting blood sugar, wheter it is greater than 120 mg/dl or not'
       self.fields['restingECG'].widget.attrs['title'] = "Resting electrocardiogram results: \nNormal: Normal ECG\nST: Having ST-T wave abnormality (T wave inversions and or ST elevation or depression of > 0.05 mV)\nLVH: Showing probable or definite left ventricular hypertrophy by Estes' criteria"
       self.fields['maxHR'].widget.attrs['title'] = 'Maximum amount of heart beats achieved per minute under maximum stress'
       self.fields['exerciseAngina'].widget.attrs['title'] = 'Wheter the patient has exercise-induced angina or not'
       self.fields['oldpeak'].widget.attrs['title'] = "ST depression.\nThe height difference (in milimiters) between the J point and the baseline (the PR segment)"
       self.fields['sT_Slope'].widget.attrs['title'] = 'The slope of the peak exercise ST segment:\nUP: Upslowing\nFLAT: Flat\nDOWN: Downslowing'
       self.fields['aiModel'].widget.attrs['title'] = 'Artificial inteligence model to use for prediction'
    class Meta:
        model = Prediction
        fields=['date_created','age','sex','chestPainType','restingBP','cholesterol','fastingBS','restingECG','maxHR','exerciseAngina','oldpeak','sT_Slope','heartDisease','heartDiseaseProb','aiModel']
        labels = {
            'date_created':'Creation date',
            'age':'Age',
            'sex':'Sex',
            'chestPainType':'Chest pain type',
            'restingBP':'Resting blood pressure',
            'cholesterol':'Serum cholesterol',
            'fastingBS':'Fasting blood sugar',
            'restingECG':'Resting electrocardiogram results',
            'maxHR':'Maximum heart rate achieved',
            'exerciseAngina':'Exercise-induced angina',
            'oldpeak':'ECG ST Segment',
            'sT_Slope':'ST Slope',
            'heartDisease':'Heart Disease',
            'heartDiseaseProb':'Probability of heart disease (%)',
            'aiModel':'AI Model'
        }
        widgets = {
            'date_created': DateInput,
        }


class EditPredictionForm(forms.ModelForm):
    newPrediction = forms.BooleanField(required=False,label="Save as new prediction")
    def __init__(self, *args, **kwargs):
       super(EditPredictionForm, self).__init__(*args, **kwargs)
       self.fields['heartDisease'].widget.attrs['disabled'] = True
       self.fields['heartDisease'].required = False
       self.fields['heartDiseaseProb'].widget.attrs['disabled'] = True
       self.fields['heartDiseaseProb'].required = False
        #Fields Description
       self.fields['age'].widget.attrs['title'] = 'Age of the patient in years'
       self.fields['sex'].widget.attrs['title'] = 'Sex of the patient'
       self.fields['chestPainType'].widget.attrs['title'] = 'Type of chest pain'
       self.fields['restingBP'].widget.attrs['title'] = 'Resting blood pressure measured in: mm/Hg'
       self.fields['cholesterol'].widget.attrs['title'] = 'Serum cholesterol measured in mm/dl'
       self.fields['fastingBS'].widget.attrs['title'] = 'Fasting blood sugar, wheter it is greater than 120 mg/dl or not'
       self.fields['restingECG'].widget.attrs['title'] = "Resting electrocardiogram results: \nNormal: Normal ECG\nST: Having ST-T wave abnormality (T wave inversions and or ST elevation or depression of > 0.05 mV)\nLVH: Showing probable or definite left ventricular hypertrophy by Estes' criteria"
       self.fields['maxHR'].widget.attrs['title'] = 'Maximum amount of heart beats achieved per minute under maximum stress'
       self.fields['exerciseAngina'].widget.attrs['title'] = 'Wheter the patient has exercise-induced angina or not'
       self.fields['oldpeak'].widget.attrs['title'] = "ST depression.\nThe height difference (in milimiters) between the J point and the baseline (the PR segment)"
       self.fields['sT_Slope'].widget.attrs['title'] = 'The slope of the peak exercise ST segment:\nUP: Upslowing\nFLAT: Flat\nDOWN: Downslowing'
       self.fields['aiModel'].widget.attrs['title'] = 'Artificial inteligence model to use for prediction'
    class Meta:
        model = Prediction
        fields=['date_created','age','sex','chestPainType','restingBP','cholesterol','fastingBS','restingECG','maxHR','exerciseAngina','oldpeak','sT_Slope','heartDisease','heartDiseaseProb','aiModel']
        labels = {
            'date_created':'Creation date',
            'age':'Age',
            'sex':'Sex',
            'chestPainType':'Chest pain type',
            'restingBP':'Resting blood pressure',
            'cholesterol':'Serum cholesterol',
            'fastingBS':'Fasting blood sugar',
            'restingECG':'Resting electrocardiogram results',
            'maxHR':'Maximum heart rate achieved',
            'exerciseAngina':'Exercise-induced angina',
            'oldpeak':'ECG ST Segment',
            'sT_Slope':'ST Slope',
            'heartDisease':'Heart Disease',
            'heartDiseaseProb':'Probability of heart disease (%)',
            'aiModel':'AI Model',
            'newPrediction': 'Save as new prediction',
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
       self.fields['heartDisease'].widget.attrs['selected'] = True
       self.fields['heartDiseaseProb'].widget.attrs['disabled'] = True
       self.fields['aiModel'].widget.attrs['disabled'] = True
        #Fields Description
       self.fields['age'].widget.attrs['title'] = 'Age of the patient in years'
       self.fields['sex'].widget.attrs['title'] = 'Sex of the patient'
       self.fields['chestPainType'].widget.attrs['title'] = 'Type of chest pain'
       self.fields['restingBP'].widget.attrs['title'] = 'Resting blood pressure measured in: mm/Hg'
       self.fields['cholesterol'].widget.attrs['title'] = 'Serum cholesterol measured in mm/dl'
       self.fields['fastingBS'].widget.attrs['title'] = 'Fasting blood sugar, wheter it is greater than 120 mg/dl or not'
       self.fields['restingECG'].widget.attrs['title'] = "Resting electrocardiogram results: \nNormal: Normal ECG\nST: Having ST-T wave abnormality (T wave inversions and or ST elevation or depression of > 0.05 mV)\nLVH: Showing probable or definite left ventricular hypertrophy by Estes' criteria"
       self.fields['maxHR'].widget.attrs['title'] = 'Maximum amount of heart beats achieved per minute under maximum stress'
       self.fields['exerciseAngina'].widget.attrs['title'] = 'Wheter the patient has exercise-induced angina or not'
       self.fields['oldpeak'].widget.attrs['title'] = "ST depression.\nThe height difference (in milimiters) between the J point and the baseline (the PR segment)"
       self.fields['sT_Slope'].widget.attrs['title'] = 'The slope of the peak exercise ST segment:\nUP: Upslowing\nFLAT: Flat\nDOWN: Downslowing'
       self.fields['aiModel'].widget.attrs['title'] = 'Artificial inteligence model used for prediction'
    class Meta:
        model = Prediction
        fields=['date_created','age','sex','chestPainType','restingBP','cholesterol','fastingBS','restingECG','maxHR','exerciseAngina','oldpeak','sT_Slope','heartDisease','heartDiseaseProb','aiModel']
        labels = {
            'date_created':'Creation date',
            'age':'Age',
            'sex':'Sex',
            'chestPainType':'Chest pain type',
            'restingBP':'Resting blood pressure',
            'cholesterol':'Serum cholesterol',
            'fastingBS':'Fasting blood sugar',
            'restingECG':'Resting electrocardiogram results',
            'maxHR':'Maximum heart rate achieved',
            'exerciseAngina':'Exercise-induced angina',
            'oldpeak':'ECG ST Segment',
            'sT_Slope':'ST Slope',
            'heartDisease':'Heart Disease',
            'heartDiseaseProb':'Probability of heart disease (%)',
            'aiModel':'AI Model'
        }
        widgets = {
            #'heartDisease': forms.TextInput(),
            'sex': forms.TextInput(),
        }       

class PredictionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(PredictionForm, self).__init__(*args, **kwargs)
       self.fields['heartDisease'].widget.attrs['disabled'] = True
       self.fields['heartDisease'].required = False
       self.fields['heartDiseaseProb'].widget.attrs['disabled'] = True
       self.fields['heartDiseaseProb'].required = False
        #Fields Description
       self.fields['age'].widget.attrs['title'] = 'Age of the patient in years'
       self.fields['sex'].widget.attrs['title'] = 'Sex of the patient'
       self.fields['chestPainType'].widget.attrs['title'] = 'Type of chest pain'
       self.fields['restingBP'].widget.attrs['title'] = 'Resting blood pressure measured in: mm/Hg'
       self.fields['cholesterol'].widget.attrs['title'] = 'Serum cholesterol measured in mm/dl'
       self.fields['fastingBS'].widget.attrs['title'] = 'Fasting blood sugar, wheter it is greater than 120 mg/dl or not'
       self.fields['restingECG'].widget.attrs['title'] = "Resting electrocardiogram results: \nNormal: Normal ECG\nST: Having ST-T wave abnormality (T wave inversions and or ST elevation or depression of > 0.05 mV)\nLVH: Showing probable or definite left ventricular hypertrophy by Estes' criteria"
       self.fields['maxHR'].widget.attrs['title'] = 'Maximum amount of heart beats achieved per minute under maximum stress'
       self.fields['exerciseAngina'].widget.attrs['title'] = 'Wheter the patient has exercise-induced angina or not'
       self.fields['oldpeak'].widget.attrs['title'] = "ST depression.\nThe height difference (in milimiters) between the J point and the baseline (the PR segment)"
       self.fields['sT_Slope'].widget.attrs['title'] = 'The slope of the peak exercise ST segment:\nUP: Upslowing\nFLAT: Flat\nDOWN: Downslowing'
       self.fields['aiModel'].widget.attrs['title'] = 'Artificial inteligence model to use for prediction'
    class Meta:
        model = Prediction
        fields=['age','sex','chestPainType','restingBP','cholesterol','fastingBS','restingECG','maxHR','exerciseAngina','oldpeak','sT_Slope','heartDisease','heartDiseaseProb','aiModel']
        labels = {
            'age':'Age',
            'sex':'Sex',
            'chestPainType':'Chest pain type',
            'restingBP':'Resting blood pressure',
            'cholesterol':'Serum cholesterol',
            'fastingBS':'Fasting blood sugar',
            'restingECG':'Resting electrocardiogram results',
            'maxHR':'Maximum heart rate achieved',
            'exerciseAngina':'Exercise-induced angina',
            'oldpeak':'ECG ST Segment',
            'sT_Slope':'ST Slope',
            'heartDisease':'Heart Disease',
            'heartDiseaseProb':'Probability of heart disease (%)',
            'aiModel':'AI Model'
        }


