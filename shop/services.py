
from django_filters import rest_framework as filters

from .models import Products


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class ProductFilter(filters.FilterSet):
    brand = CharFilterInFilter(field_name='brand__name', lookup_expr='in')
    color = CharFilterInFilter(field_name='color__name', lookup_expr='in')
    price = filters.RangeFilter()
    gender = CharFilterInFilter(field_name='gender__name', lookup_expr='in')

    class Meta:
        model = Products
        fields = ['brand', 'price','gender']