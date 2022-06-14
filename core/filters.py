from django_filters import rest_framework as filters

from core.models import Examination

class ExaminationFilterSet(filters.FilterSet):

    class Meta:
        model = Examination
        fields = [
            'altered'
        ]