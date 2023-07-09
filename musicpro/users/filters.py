from django_filters import rest_framework as filters
from .models import Comuna

class Comuna_Filter(filters.FilterSet):
    id = filters.NumberFilter(field_name='id', lookup_expr='exact')
    region = filters.NumberFilter(field_name='id_region', lookup_expr='exact')


    class Meta:
        model = Comuna
        fields = ['id', 'id_region']
        field_mappings = {
            'id': 'id',
            'region': 'id_region',

        }
