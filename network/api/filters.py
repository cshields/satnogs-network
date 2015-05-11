import django_filters

from network.base.models import Data


class DataViewFilter(django_filters.FilterSet):
    class Meta:
        model = Data
        fields = ['start', 'end', 'ground_station']
