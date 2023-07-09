from django_filters import rest_framework as filters
from .models import Order

class Order_Filter(filters.FilterSet):
    id = filters.NumberFilter(field_name='id', lookup_expr='exact')
    status = filters.CharFilter(field_name='status', lookup_expr='exact')

    class Meta:
        model = Product
        fields = ['id', 'status']
        field_mappings = {
            'id': 'id',
            'status': 'status',
        }
