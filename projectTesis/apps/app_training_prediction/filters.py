from django import forms
import django_filters
from .models import PredictionToTrain
from django.utils.translation import gettext as _


class DateInput(forms.DateInput):
    input_type = 'date'

class PredictionToTrainFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(PredictionToTrainFilter, self).__init__(*args, **kwargs)
        self.filters['dateFilter'].label = _("Date")+":"
        self.filters['f_name_filter'].label = _("Name")+":"
        self.filters['l_name_filter'].label = _("Last name")+":"
    dateFilter = django_filters.DateFilter(
        field_name="date_created",
        lookup_expr="iexact",
        widget=DateInput,
        label=_("Date")+":"
    )
    f_name_filter = django_filters.CharFilter(
        field_name = 'prediction__Patient__first_name',
        lookup_expr ='iexact',
        label = _('Name')+":",
        distinct = True,
    )
    l_name_filter = django_filters.CharFilter(
        field_name = 'prediction__Patient__last_name',
        lookup_expr ='iexact',
        label = _('Last name')+":",
        distinct = True,
    )
    class Meta:
        model = PredictionToTrain
        fields= ['date_created',
                'prediction__Patient__first_name',
                'prediction__Patient__last_name']
        widgets = {
            'date_created' : DateInput()
        }