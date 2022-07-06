from random import choices
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')


class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

hd_choices = (
    (0, 'No'),
    (1, _('Yes')),
    (3, _('All')),
)
x_label_choices = (
    (_('Age'), _('Age')),
    (_('RestingBP'), _('RestingBP')),
    (_('Cholesterol'), _('Cholesterol')),
    (_('MaxHR'), _('MaxHR')),
    (_('Oldpeak'), _('Oldpeak')),
)

hue_choices = (
    (_('Sex'), _('Sex')),
    (_('ChestPainType'), _('ChestPainType')),
    (_('FastingBS'), _('FastingBS')),
    (_('RestingECG'), _('RestingECG')),
    (_('ExerciseAngina'), _('ExerciseAngina')),
    (_('ST_Slope'), _('ST_Slope')),
)

bar_choices = (
    (_('Age'), _('Age')),
    (_('Sex'), _('Sex')),
    (_('ChestPainType'), _('ChestPainType')),
    (_('RestingBP'), _('RestingBP')),
    (_('Cholesterol'), _('Cholesterol')),
    (_('FastingBS'), _('FastingBS')),
    (_('RestingECG'), _('RestingECG')),
    (_('MaxHR'), _('MaxHR')),
    (_('ExerciseAngina'), _('ExerciseAngina')),
    (_('Oldpeak'), _('Oldpeak')),
    (_('ST_Slope'), _('ST_Slope')),
)

class DataAnalyticsBoxForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DataAnalyticsBoxForm, self).__init__(*args, **kwargs)   
        self.fields['output_box'].label = _('Heart Disease')
        self.fields['x_label_box'].label = _('Variable (X Axis)')
        self.fields['hue_box'].label = _('Groups')  

    output_box = forms.ChoiceField(choices=hd_choices, required=False)
    x_label_box = forms.ChoiceField(choices=x_label_choices, required=False)
    hue_box = forms.ChoiceField(choices=hue_choices, required=False)

class DataAnalyticsHistForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DataAnalyticsHistForm, self).__init__(*args, **kwargs)   
        self.fields['output'].label = _('Heart Disease')
        self.fields['x_label'].label = _('Variable (X Axis)')
        self.fields['hue'].label = _('Groups')  

    output = forms.ChoiceField(choices=hd_choices, required=False)
    x_label = forms.ChoiceField(choices=x_label_choices, required=False)
    hue = forms.ChoiceField(choices=hue_choices, required=False)

class DataAnalyticsBarsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DataAnalyticsBarsForm, self).__init__(*args, **kwargs)   
        self.fields['output_bar'].label = _('Heart Disease')
        self.fields['x_label_bar'].label = _('Variable (X Axis)')

    output_bar = forms.ChoiceField(choices=hd_choices, required=False)
    x_label_bar = forms.ChoiceField(choices=bar_choices, required=False)