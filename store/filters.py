from django_filters.rest_framework import FilterSet, NumberFilter,CharFilter,DateFilter
from .models import Box

class BoxFilter(FilterSet):
    length_more_than = NumberFilter(field_name='length', lookup_expr='gt')
    length_less_than = NumberFilter(field_name='length', lookup_expr='lt')
    breadth_more_than = NumberFilter(field_name='breadth', lookup_expr='gt')
    breadth_less_than = NumberFilter(field_name='breadth', lookup_expr='lt')
    height_more_than = NumberFilter(field_name='height', lookup_expr='gt')
    height_less_than = NumberFilter(field_name='height', lookup_expr='lt')
    area_more_than = NumberFilter(field_name='area', lookup_expr='gt')
    area_less_than = NumberFilter(field_name='area', lookup_expr='lt')
    volume_more_than = NumberFilter(field_name='volume', lookup_expr='gt')
    volume_less_than = NumberFilter(field_name='volume', lookup_expr='lt')
    created_by = CharFilter(field_name='creator__username')
    created_before = DateFilter(field_name='created_at', lookup_expr='lt')
    created_after = DateFilter(field_name='created_at', lookup_expr='gt')

    class Meta:
        model = Box
        fields=[]


class BoxUserFilter(FilterSet):
    length_more_than = NumberFilter(field_name='length', lookup_expr='gt')
    length_less_than = NumberFilter(field_name='length', lookup_expr='lt')
    breadth_more_than = NumberFilter(field_name='breadth', lookup_expr='gt')
    breadth_less_than = NumberFilter(field_name='breadth', lookup_expr='lt')
    height_more_than = NumberFilter(field_name='height', lookup_expr='gt')
    height_less_than = NumberFilter(field_name='height', lookup_expr='lt')
    area_more_than = NumberFilter(field_name='area', lookup_expr='gt')
    area_less_than = NumberFilter(field_name='area', lookup_expr='lt')
    volume_more_than = NumberFilter(field_name='volume', lookup_expr='gt')
    volume_less_than = NumberFilter(field_name='volume', lookup_expr='lt')

    class Meta:
        model = Box
        fields=[]