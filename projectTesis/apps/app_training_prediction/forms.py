from django import forms
from .models import PredictionToTrain
from django.utils.translation import gettext as _


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
        self.fields['restingBP'].label = _('Resting systolic blood pressure (mm/Hg)')
        self.fields['cholesterol'].label = _('Serum cholesterol (mm/dl)')
        self.fields['fastingBS'].label = _('Fasting blood sugar')
        self.fields['restingECG'].label = _(
            "Resting electrocardiogram results")
        self.fields['maxHR'].label = _('Maximum heart rate achieved')
        self.fields['exerciseAngina'].label = _('Exercise-induced angina')
        self.fields['oldpeak'].label = _("ECG ST Segment (milimeters)")
        self.fields['sT_Slope'].label = _('ST Slope')
        self.fields['heartDisease'].label = _('Heart Disease')
        self.fields['aiModel'].label = _('Machine learning model')
        # Fields Description
        self.fields['age'].widget.attrs['title'] = _(
            'Age of the patient in years')
        self.fields['sex'].widget.attrs['title'] = _('Sex of the patient')
        self.fields['chestPainType'].widget.attrs['title'] = _(
            'Type of chest pain')
        self.fields['restingBP'].widget.attrs['title'] = _(
            'Resting systolic blood pressure measured in: mm/Hg')
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
            'The slope of the ST segment during ECG stress test:\nUP: Upslowing\nFLAT: Flat\nDOWN: Downslowing')
        self.fields['aiModel'].widget.attrs['title'] = _(
            'Machine learning model to use for prediction')

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
        self.fields['restingBP'].label = _('Resting systolic blood pressure (mm/Hg)')
        self.fields['cholesterol'].label = _('Serum cholesterol (mm/dl)')
        self.fields['fastingBS'].label = _('Fasting blood sugar')
        self.fields['restingECG'].label = _(
            "Resting electrocardiogram results")
        self.fields['maxHR'].label = _('Maximum heart rate achieved')
        self.fields['exerciseAngina'].label = _('Exercise-induced angina')
        self.fields['oldpeak'].label = _("ECG ST Segment (milimeters)")
        self.fields['sT_Slope'].label = _('ST Slope')
        self.fields['heartDisease'].label = _('Heart Disease')
        self.fields['aiModel'].label = _('Machine learning model')
        # Fields Description
        self.fields['age'].widget.attrs['title'] = _(
            'Age of the patient in years')
        self.fields['sex'].widget.attrs['title'] = _('Sex of the patient')
        self.fields['chestPainType'].widget.attrs['title'] = _(
            'Type of chest pain')
        self.fields['restingBP'].widget.attrs['title'] = _(
            'Resting systolic blood pressure measured in: mm/Hg')
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
            'The slope of the ST segment during ECG stress test:\nUP: Upslowing\nFLAT: Flat\nDOWN: Downslowing')
        self.fields['aiModel'].widget.attrs['title'] = _(
            'Machine learning model to use for prediction')

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
