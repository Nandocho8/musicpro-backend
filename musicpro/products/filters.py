from django_filters import rest_framework as filters
from .models import Product

class Product_Filter(filters.FilterSet):
    id = filters.NumberFilter(field_name='id', lookup_expr='exact')
    subcategory = filters.CharFilter(field_name='subcategory__name', lookup_expr='icontains')
    category = filters.CharFilter(field_name='subcategory__category__name', lookup_expr='icontains')
    type = filters.CharFilter(field_name='subcategory__category__type__name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['id', 'subcategory']
        field_mappings = {
            'id': 'id',
            'subcategory': 'subcategory__name',
            'category': 'subcategory__category__name',
            'type': 'subcategory__category__type__name',
        }
