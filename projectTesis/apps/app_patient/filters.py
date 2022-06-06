import django_filters
from .models import Patient
from django.utils.translation import gettext as _


class PatientFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(PatientFilter, self).__init__(*args, **kwargs)
        self.filters['nameFilter'].label = _("Name")+":"
        self.filters['idFilter'].label = _("Id")+":"
        self.filters['hdProbFilter'].label = _("Probability > than")+":"

    nameFilter = django_filters.CharFilter(
        field_name = 'first_name',
        lookup_expr ='iexact',
        label = _('Name')+":",
        distinct = True,
    )
    idFilter = django_filters.CharFilter(
        field_name = 'id_number',
        lookup_expr ='iexact',
        label = _('Id')+":",
        distinct = True,
    )
    hdProbFilter = django_filters.NumberFilter(
        field_name = 'last_prediction_prob',
        lookup_expr ='gt',
        label = _('Probability > than')+":",
        distinct = True,
    )
    class Meta:
        model = Patient
        fields = ['first_name','id_number','last_prediction_prob']
