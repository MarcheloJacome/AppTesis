from django import forms
from .models import Patient
from django.utils.translation import gettext as _

class DateInput(forms.DateInput):
    input_type = 'date'

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
        self.fields['height'].label = _('Height (cm)')
        self.fields['weight'].label = _('Weight (kg)')

    class Meta:
        model = Patient
        fields = [
            'first_name',
            'last_name',
            'id_number',
            'city',
            'address',
            'phone_number',
            'height',
            'weight',
        ]

class DetailPatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DetailPatientForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['readonly'] = True
        self.fields['last_name'].widget.attrs['readonly'] = True
        self.fields['id_number'].widget.attrs['readonly'] = True
        self.fields['city'].widget.attrs['readonly'] = True
        self.fields['address'].widget.attrs['readonly'] = True
        self.fields['phone_number'].widget.attrs['readonly'] = True
        self.fields['height'].widget.attrs['readonly'] = True
        self.fields['weight'].widget.attrs['readonly'] = True
        # labels
        self.fields['first_name'].label = _('First Name')
        self.fields['last_name'].label = _('Last Name')
        self.fields['id_number'].label = _('ID Number')
        self.fields['city'].label = _('City')
        self.fields['address'].label = _('Adress')
        self.fields['phone_number'].label = _('Phone Number')
        self.fields['height'].label = _('Height (cm)')
        self.fields['weight'].label = _('Weight (kg)')

    class Meta:
        model = Patient
        fields = [
            'first_name',
            'last_name',
            'id_number',
            'city',
            'address',
            'phone_number',
            'height',
            'weight',
        ]

