from django import forms
import django_filters
from apps.app1.models import *

class PatientFilter(django_filters.FilterSet):
    nameFilter = django_filters.CharFilter(
        field_name = 'first_name',
        lookup_expr ='iexact',
        label = 'Name',
    )
    idFilter = django_filters.CharFilter(
        field_name = 'id_number',
        lookup_expr ='iexact',
        label = 'Id',
    )
    class Meta:
        model = Patient
        fields = ['first_name','id_number']

class DateInput(forms.DateInput):
    input_type = 'date'

class PredictionFilter(django_filters.FilterSet):
    dateFilter = django_filters.DateFilter(
        field_name="date_created",
        lookup_expr="iexact",
        widget=DateInput,
        label="Date"
    )
    class Meta:
        model = Prediction
        fields= ['date_created']
        widgets = {
            'date_created' : DateInput()
        }