from random import choices
from django import forms
from django.forms import fields, widgets
from .models import Patient, Prediction, PredictionToTrain
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.utils.translation import gettext as _


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')


class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class CreatePatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreatePatientForm, self).__init__(*args, **kwargs)
        # labels
        self.fields['first_name'].label = _('First Name')
        self.fields['last_name'].label = _('Last Name')
        self.fields['id_number'].label = _('ID Number')
        self.fields['city'].label = _('City')
        self.fields['address'].label = _('Adress')
        self.fields['phone_number'].label = _('Phone Number')
        self.fields['height'].label = _('Height')
        self.fields['weight'].label = _('Weight')

    class Meta:
        model = Patient
        fields = [
            'first_name',
            'last_name',
            'id_number',
            # 'sex',
            'city',
            'address',
            'phone_number',
            # 'age',
            'height',
            'weight',
        ]



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
        # labels
        self.fields['first_name'].label = _('First Name')
        self.fields['last_name'].label = _('Last Name')
        self.fields['id_number'].label = _('ID Number')
        self.fields['city'].label = _('City')
        self.fields['address'].label = _('Adress')
        self.fields['phone_number'].label = _('Phone Number')
        self.fields['height'].label = _('Height')
        self.fields['weight'].label = _('Weight')

    class Meta:
        model = Patient
        fields = [
            'first_name',
            'last_name',
            'id_number',
            # 'sex',
            'city',
            'address',
            'phone_number',
            # 'age',
            'height',
            'weight',
        ]



class MakePredictionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MakePredictionForm, self).__init__(*args, **kwargs)
        self.fields['heartDisease'].widget.attrs['disabled'] = True
        self.fields['heartDisease'].required = False
        self.fields['heartDiseaseProb'].widget.attrs['disabled'] = True
        self.fields['heartDiseaseProb'].required = False

        # labels
        self.fields['age'].label = _('Age')
        self.fields['sex'].label = _('Sex')
        self.fields['chestPainType'].label = _('Chest pain type')
        self.fields['restingBP'].label = _('Resting blood pressure')
        self.fields['cholesterol'].label = _('Serum cholesterol')
        self.fields['fastingBS'].label = _('Fasting blood sugar')
        self.fields['restingECG'].label = _(
            "Resting electrocardiogram results")
        self.fields['maxHR'].label = _('Maximum heart rate achieved')
        self.fields['exerciseAngina'].label = _('Exercise-induced angina')
        self.fields['oldpeak'].label = _("ECG ST Segment")
        self.fields['sT_Slope'].label = _('ST Slope')
        self.fields['heartDisease'].label = _('Heart Disease')
        self.fields['heartDiseaseProb'].label = _(
            'Probability of heart disease (%)')
        self.fields['aiModel'].label = _('AI Model')
        # Fields Description
        self.fields['age'].widget.attrs['title'] = _(
            'Age of the patient in years')
        self.fields['sex'].widget.attrs['title'] = _('Sex of the patient')
        self.fields['chestPainType'].widget.attrs['title'] = _(
            'Type of chest pain')
        self.fields['restingBP'].widget.attrs['title'] = _(
            'Resting blood pressure measured in: mm/Hg')
        self.fields['cholesterol'].widget.attrs['title'] = _(
            'Serum cholesterol measured in mm/dl')
        self.fields['fastingBS'].widget.attrs['title'] = _(
            'Fasting blood sugar, wheter it is greater than 120 mg/dl or not')
        self.fields['restingECG'].widget.attrs['title'] = _(
            "Resting electrocardiogram results: \nNormal: Normal ECG\nST: Having ST-T wave abnormality (T wave inversions and or ST elevation or depression of > 0.05 mV)\nLVH: Showing probable or definite left ventricular hypertrophy by Estes' criteria")
        self.fields['maxHR'].widget.attrs['title'] = _(
            'Maximum amount of heart beats achieved per minute under maximum stress')
        self.fields['exerciseAngina'].widget.attrs['title'] = _(
            'Wheter the patient has exercise-induced angina or not')
        self.fields['oldpeak'].widget.attrs['title'] = _(
            "ST depression.\nThe height difference (in milimiters) between the J point and the baseline (the PR segment)")
        self.fields['sT_Slope'].widget.attrs['title'] = _(
            'The slope of the peak exercise ST segment:\nUP: Upslowing\nFLAT: Flat\nDOWN: Downslowing')
        self.fields['aiModel'].widget.attrs['title'] = _(
            'Artificial inteligence model to use for prediction')

    class Meta:
        model = Prediction
        fields = ['age', 'sex', 'chestPainType', 'restingBP', 'cholesterol', 'fastingBS', 'restingECG',
                  'maxHR', 'exerciseAngina', 'oldpeak', 'sT_Slope', 'heartDisease', 'heartDiseaseProb', 'aiModel']


class EditPredictionForm(forms.ModelForm):
    newPrediction = forms.BooleanField(
        required=False, label="Save as new prediction")

    def __init__(self, *args, **kwargs):
        super(EditPredictionForm, self).__init__(*args, **kwargs)
        self.fields['date_created'].widget.attrs['readonly'] = True
        self.fields['heartDisease'].widget.attrs['disabled'] = True
        self.fields['heartDisease'].required = False
        self.fields['heartDiseaseProb'].widget.attrs['disabled'] = True
        self.fields['heartDiseaseProb'].required = False
        # labels
        self.fields['date_created'].label = _('Creation date')
        self.fields['age'].label = _('Age')
        self.fields['sex'].label = _('Sex')
        self.fields['chestPainType'].label = _('Chest pain type')
        self.fields['restingBP'].label = _('Resting blood pressure')
        self.fields['cholesterol'].label = _('Serum cholesterol')
        self.fields['fastingBS'].label = _('Fasting blood sugar')
        self.fields['restingECG'].label = _(
            "Resting electrocardiogram results")
        self.fields['maxHR'].label = _('Maximum heart rate achieved')
        self.fields['exerciseAngina'].label = _('Exercise-induced angina')
        self.fields['oldpeak'].label = _("ECG ST Segment")
        self.fields['sT_Slope'].label = _('ST Slope')
        self.fields['heartDisease'].label = _('Heart Disease')
        self.fields['heartDiseaseProb'].label = _(
            'Probability of heart disease (%)')
        self.fields['aiModel'].label = _('AI Model')
        self.fields['newPrediction'].label = _('Save as new prediction')
        # Fields Description
        self.fields['age'].widget.attrs['title'] = _(
            'Age of the patient in years')
        self.fields['sex'].widget.attrs['title'] = _('Sex of the patient')
        self.fields['chestPainType'].widget.attrs['title'] = _(
            'Type of chest pain')
        self.fields['restingBP'].widget.attrs['title'] = _(
            'Resting blood pressure measured in: mm/Hg')
        self.fields['cholesterol'].widget.attrs['title'] = _(
            'Serum cholesterol measured in mm/dl')
        self.fields['fastingBS'].widget.attrs['title'] = _(
            'Fasting blood sugar, wheter it is greater than 120 mg/dl or not')
        self.fields['restingECG'].widget.attrs['title'] = _(
            "Resting electrocardiogram results: \nNormal: Normal ECG\nST: Having ST-T wave abnormality (T wave inversions and or ST elevation or depression of > 0.05 mV)\nLVH: Showing probable or definite left ventricular hypertrophy by Estes' criteria")
        self.fields['maxHR'].widget.attrs['title'] = _(
            'Maximum amount of heart beats achieved per minute under maximum stress')
        self.fields['exerciseAngina'].widget.attrs['title'] = _(
            'Wheter the patient has exercise-induced angina or not')
        self.fields['oldpeak'].widget.attrs['title'] = _(
            "ST depression.\nThe height difference (in milimiters) between the J point and the baseline (the PR segment)")
        self.fields['sT_Slope'].widget.attrs['title'] = _(
            'The slope of the peak exercise ST segment:\nUP: Upslowing\nFLAT: Flat\nDOWN: Downslowing')
        self.fields['aiModel'].widget.attrs['title'] = _(
            'Artificial inteligence model to use for prediction')

    class Meta:
        model = Prediction
        fields = ['date_created', 'age', 'sex', 'chestPainType', 'restingBP', 'cholesterol', 'fastingBS', 'restingECG',
                  'maxHR', 'exerciseAngina', 'oldpeak', 'sT_Slope', 'heartDisease', 'heartDiseaseProb', 'aiModel']


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
        # labels
        self.fields['date_created'].label = _('Creation date')
        self.fields['age'].label = _('Age')
        self.fields['sex'].label = _('Sex')
        self.fields['chestPainType'].label = _('Chest pain type')
        self.fields['restingBP'].label = _('Resting blood pressure')
        self.fields['cholesterol'].label = _('Serum cholesterol')
        self.fields['fastingBS'].label = _('Fasting blood sugar')
        self.fields['restingECG'].label = _(
            "Resting electrocardiogram results")
        self.fields['maxHR'].label = _('Maximum heart rate achieved')
        self.fields['exerciseAngina'].label = _('Exercise-induced angina')
        self.fields['oldpeak'].label = _("ECG ST Segment")
        self.fields['sT_Slope'].label = _('ST Slope')
        self.fields['heartDisease'].label = _('Heart Disease')
        self.fields['heartDiseaseProb'].label = _(
            'Probability of heart disease (%)')
        self.fields['aiModel'].label = _('AI Model')
        # Fields Description
        self.fields['age'].widget.attrs['title'] = _(
            'Age of the patient in years')
        self.fields['sex'].widget.attrs['title'] = _('Sex of the patient')
        self.fields['chestPainType'].widget.attrs['title'] = _(
            'Type of chest pain')
        self.fields['restingBP'].widget.attrs['title'] = _(
            'Resting blood pressure measured in: mm/Hg')
        self.fields['cholesterol'].widget.attrs['title'] = _(
            'Serum cholesterol measured in mm/dl')
        self.fields['fastingBS'].widget.attrs['title'] = _(
            'Fasting blood sugar, wheter it is greater than 120 mg/dl or not')
        self.fields['restingECG'].widget.attrs['title'] = _(
            "Resting electrocardiogram results: \nNormal: Normal ECG\nST: Having ST-T wave abnormality (T wave inversions and or ST elevation or depression of > 0.05 mV)\nLVH: Showing probable or definite left ventricular hypertrophy by Estes' criteria")
        self.fields['maxHR'].widget.attrs['title'] = _(
            'Maximum amount of heart beats achieved per minute under maximum stress')
        self.fields['exerciseAngina'].widget.attrs['title'] = _(
            'Wheter the patient has exercise-induced angina or not')
        self.fields['oldpeak'].widget.attrs['title'] = _(
            "ST depression.\nThe height difference (in milimiters) between the J point and the baseline (the PR segment)")
        self.fields['sT_Slope'].widget.attrs['title'] = _(
            'The slope of the peak exercise ST segment:\nUP: Upslowing\nFLAT: Flat\nDOWN: Downslowing')
        self.fields['aiModel'].widget.attrs['title'] = _(
            'Artificial inteligence model to use for prediction')

    class Meta:
        model = Prediction
        fields = ['date_created', 'age', 'sex', 'chestPainType', 'restingBP', 'cholesterol', 'fastingBS', 'restingECG',
                  'maxHR', 'exerciseAngina', 'oldpeak', 'sT_Slope', 'heartDisease', 'heartDiseaseProb', 'aiModel']


class PredictionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PredictionForm, self).__init__(*args, **kwargs)
        self.fields['heartDisease'].widget.attrs['disabled'] = True
        self.fields['heartDisease'].required = False
        self.fields['heartDiseaseProb'].widget.attrs['disabled'] = True
        self.fields['heartDiseaseProb'].required = False
        # labels
        self.fields['age'].label = _('Age')
        self.fields['sex'].label = _('Sex')
        self.fields['chestPainType'].label = _('Chest pain type')
        self.fields['restingBP'].label = _('Resting blood pressure')
        self.fields['cholesterol'].label = _('Serum cholesterol')
        self.fields['fastingBS'].label = _('Fasting blood sugar')
        self.fields['restingECG'].label = _(
            "Resting electrocardiogram results")
        self.fields['maxHR'].label = _('Maximum heart rate achieved')
        self.fields['exerciseAngina'].label = _('Exercise-induced angina')
        self.fields['oldpeak'].label = _("ECG ST Segment")
        self.fields['sT_Slope'].label = _('ST Slope')
        self.fields['heartDisease'].label = _('Heart Disease')
        self.fields['heartDiseaseProb'].label = _(
            'Probability of heart disease (%)')
        self.fields['aiModel'].label = _('AI Model')
        # Fields Description
        self.fields['age'].widget.attrs['title'] = _(
            'Age of the patient in years')
        self.fields['sex'].widget.attrs['title'] = _('Sex of the patient')
        self.fields['chestPainType'].widget.attrs['title'] = _(
            'Type of chest pain')
        self.fields['restingBP'].widget.attrs['title'] = _(
            'Resting blood pressure measured in: mm/Hg')
        self.fields['cholesterol'].widget.attrs['title'] = _(
            'Serum cholesterol measured in mm/dl')
        self.fields['fastingBS'].widget.attrs['title'] = _(
            'Fasting blood sugar, wheter it is greater than 120 mg/dl or not')
        self.fields['restingECG'].widget.attrs['title'] = _(
            "Resting electrocardiogram results: \nNormal: Normal ECG\nST: Having ST-T wave abnormality (T wave inversions and or ST elevation or depression of > 0.05 mV)\nLVH: Showing probable or definite left ventricular hypertrophy by Estes' criteria")
        self.fields['maxHR'].widget.attrs['title'] = _(
            'Maximum amount of heart beats achieved per minute under maximum stress')
        self.fields['exerciseAngina'].widget.attrs['title'] = _(
            'Wheter the patient has exercise-induced angina or not')
        self.fields['oldpeak'].widget.attrs['title'] = _(
            "ST depression.\nThe height difference (in milimiters) between the J point and the baseline (the PR segment)")
        self.fields['sT_Slope'].widget.attrs['title'] = _(
            'The slope of the peak exercise ST segment:\nUP: Upslowing\nFLAT: Flat\nDOWN: Downslowing')
        self.fields['aiModel'].widget.attrs['title'] = _(
            'Artificial inteligence model to use for prediction')

    class Meta:
        model = Prediction
        fields = ['age', 'sex', 'chestPainType', 'restingBP', 'cholesterol', 'fastingBS', 'restingECG',
                  'maxHR', 'exerciseAngina', 'oldpeak', 'sT_Slope', 'heartDisease', 'heartDiseaseProb', 'aiModel']


class DetailPredictionToTrainForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DetailPredictionToTrainForm, self).__init__(*args, **kwargs)
        self.fields['date_created'].widget.attrs['readonly'] = True
        self.fields['age'].widget.attrs['readonly'] = True
        self.fields['sex'].widget.attrs['disabled'] = True
        self.fields['chestPainType'].widget.attrs['disabled'] = True
        self.fields['restingBP'].widget.attrs['disabled'] = True
        self.fields['cholesterol'].widget.attrs['readonly'] = True
        self.fields['fastingBS'].widget.attrs['disabled'] = True
        self.fields['restingECG'].widget.attrs['disabled'] = True
        self.fields['maxHR'].widget.attrs['readonly'] = True
        self.fields['exerciseAngina'].widget.attrs['disabled'] = True
        self.fields['oldpeak'].widget.attrs['readonly'] = True
        self.fields['sT_Slope'].widget.attrs['disabled'] = True
        self.fields['heartDisease'].widget.attrs['disabled'] = True
        self.fields['heartDisease'].widget.attrs['selected'] = True
        self.fields['aiModel'].widget.attrs['disabled'] = True
        # labels
        self.fields['date_created'].label = _('Creation date')
        self.fields['age'].label = _('Age')
        self.fields['sex'].label = _('Sex')
        self.fields['chestPainType'].label = _('Chest pain type')
        self.fields['restingBP'].label = _('Resting blood pressure')
        self.fields['cholesterol'].label = _('Serum cholesterol')
        self.fields['fastingBS'].label = _('Fasting blood sugar')
        self.fields['restingECG'].label = _(
            "Resting electrocardiogram results")
        self.fields['maxHR'].label = _('Maximum heart rate achieved')
        self.fields['exerciseAngina'].label = _('Exercise-induced angina')
        self.fields['oldpeak'].label = _("ECG ST Segment")
        self.fields['sT_Slope'].label = _('ST Slope')
        self.fields['heartDisease'].label = _('Heart Disease')
        self.fields['aiModel'].label = _('AI Model')
        # Fields Description
        self.fields['age'].widget.attrs['title'] = _(
            'Age of the patient in years')
        self.fields['sex'].widget.attrs['title'] = _('Sex of the patient')
        self.fields['chestPainType'].widget.attrs['title'] = _(
            'Type of chest pain')
        self.fields['restingBP'].widget.attrs['title'] = _(
            'Resting blood pressure measured in: mm/Hg')
        self.fields['cholesterol'].widget.attrs['title'] = _(
            'Serum cholesterol measured in mm/dl')
        self.fields['fastingBS'].widget.attrs['title'] = _(
            'Fasting blood sugar, wheter it is greater than 120 mg/dl or not')
        self.fields['restingECG'].widget.attrs['title'] = _(
            "Resting electrocardiogram results: \nNormal: Normal ECG\nST: Having ST-T wave abnormality (T wave inversions and or ST elevation or depression of > 0.05 mV)\nLVH: Showing probable or definite left ventricular hypertrophy by Estes' criteria")
        self.fields['maxHR'].widget.attrs['title'] = _(
            'Maximum amount of heart beats achieved per minute under maximum stress')
        self.fields['exerciseAngina'].widget.attrs['title'] = _(
            'Wheter the patient has exercise-induced angina or not')
        self.fields['oldpeak'].widget.attrs['title'] = _(
            "ST depression.\nThe height difference (in milimiters) between the J point and the baseline (the PR segment)")
        self.fields['sT_Slope'].widget.attrs['title'] = _(
            'The slope of the peak exercise ST segment:\nUP: Upslowing\nFLAT: Flat\nDOWN: Downslowing')
        self.fields['aiModel'].widget.attrs['title'] = _(
            'Artificial inteligence model to use for prediction')

    class Meta:
        model = PredictionToTrain
        fields = ['date_created', 'age', 'sex', 'chestPainType', 'restingBP', 'cholesterol', 'fastingBS',
                  'restingECG', 'maxHR', 'exerciseAngina', 'oldpeak', 'sT_Slope', 'heartDisease', 'aiModel']


class EditPredictionToTrainForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditPredictionToTrainForm, self).__init__(*args, **kwargs)
        self.fields['date_created'].widget.attrs['readonly'] = True
        self.fields['age'].widget.attrs['readonly'] = True
        self.fields['sex'].widget.attrs['disabled'] = True
        self.fields['chestPainType'].widget.attrs['disabled'] = True
        self.fields['restingBP'].widget.attrs['readonly'] = True
        self.fields['cholesterol'].widget.attrs['readonly'] = True
        self.fields['fastingBS'].widget.attrs['disabled'] = True
        self.fields['restingECG'].widget.attrs['disabled'] = True
        self.fields['maxHR'].widget.attrs['readonly'] = True
        self.fields['exerciseAngina'].widget.attrs['disabled'] = True
        self.fields['oldpeak'].widget.attrs['readonly'] = True
        self.fields['sT_Slope'].widget.attrs['disabled'] = True
        self.fields['aiModel'].widget.attrs['disabled'] = True
        # labels
        self.fields['date_created'].label = _('Creation date')
        self.fields['age'].label = _('Age')
        self.fields['sex'].label = _('Sex')
        self.fields['chestPainType'].label = _('Chest pain type')
        self.fields['restingBP'].label = _('Resting blood pressure')
        self.fields['cholesterol'].label = _('Serum cholesterol')
        self.fields['fastingBS'].label = _('Fasting blood sugar')
        self.fields['restingECG'].label = _(
            "Resting electrocardiogram results")
        self.fields['maxHR'].label = _('Maximum heart rate achieved')
        self.fields['exerciseAngina'].label = _('Exercise-induced angina')
        self.fields['oldpeak'].label = _("ECG ST Segment")
        self.fields['sT_Slope'].label = _('ST Slope')
        self.fields['heartDisease'].label = _('Heart Disease')
        self.fields['aiModel'].label = _('AI Model')
        # Fields Description
        self.fields['age'].widget.attrs['title'] = _(
            'Age of the patient in years')
        self.fields['sex'].widget.attrs['title'] = _('Sex of the patient')
        self.fields['chestPainType'].widget.attrs['title'] = _(
            'Type of chest pain')
        self.fields['restingBP'].widget.attrs['title'] = _(
            'Resting blood pressure measured in: mm/Hg')
        self.fields['cholesterol'].widget.attrs['title'] = _(
            'Serum cholesterol measured in mm/dl')
        self.fields['fastingBS'].widget.attrs['title'] = _(
            'Fasting blood sugar, wheter it is greater than 120 mg/dl or not')
        self.fields['restingECG'].widget.attrs['title'] = _(
            "Resting electrocardiogram results: \nNormal: Normal ECG\nST: Having ST-T wave abnormality (T wave inversions and or ST elevation or depression of > 0.05 mV)\nLVH: Showing probable or definite left ventricular hypertrophy by Estes' criteria")
        self.fields['maxHR'].widget.attrs['title'] = _(
            'Maximum amount of heart beats achieved per minute under maximum stress')
        self.fields['exerciseAngina'].widget.attrs['title'] = _(
            'Wheter the patient has exercise-induced angina or not')
        self.fields['oldpeak'].widget.attrs['title'] = _(
            "ST depression.\nThe height difference (in milimiters) between the J point and the baseline (the PR segment)")
        self.fields['sT_Slope'].widget.attrs['title'] = _(
            'The slope of the peak exercise ST segment:\nUP: Upslowing\nFLAT: Flat\nDOWN: Downslowing')
        self.fields['aiModel'].widget.attrs['title'] = _(
            'Artificial inteligence model to use for prediction')

    class Meta:
        model = PredictionToTrain
        fields = ['date_created', 'age', 'sex', 'chestPainType', 'restingBP', 'cholesterol', 'fastingBS',
                  'restingECG', 'maxHR', 'exerciseAngina', 'oldpeak', 'sT_Slope', 'heartDisease', 'aiModel']


class EditPredictionToTrainForm1(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditPredictionToTrainForm1, self).__init__(*args, **kwargs)
        # labels
        self.fields['heartDisease'].label = _('Heart Disease')

    class Meta:
        model = PredictionToTrain
        fields = ['heartDisease']
