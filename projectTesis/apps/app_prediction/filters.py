from django import forms
import django_filters
from .models import Prediction
from django.utils.translation import gettext as _

class DateInput(forms.DateInput):
    input_type = 'date'

class PredictionFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(PredictionFilter, self).__init__(*args, **kwargs)
        self.filters['dateFilter'].label = _("Date")+":"
    dateFilter = django_filters.DateFilter(
        field_name="date_created",
        lookup_expr="iexact",
        widget=DateInput,
        label=_("Date")+":",
    )
    class Meta:
        model = Prediction
        fields= ['date_created']
        widgets = {
            'date_created' : DateInput()
        }

