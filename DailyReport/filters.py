from django_filters import FilterSet
from django_filters import filters
from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):

    name = filters.get_model_field(Item, 'name')
    created_at = filters.DateFilter(label='日(yyyy-mm-dd)', lookup_expr='contains')
    memo = filters.CharFilter(label='備考', lookup_expr='contains')

    order_by = MyOrderingFilter(

        fields=(
            ('name', 'name'),
        ),
        field_labels={
            'name': '氏名',
        },
        label='並び順'
    )

    class Meta:
        model = Item
        fields = ('name', 'memo', 'created_at')
