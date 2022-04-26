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