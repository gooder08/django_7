from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = filters.DateFromToRangeFilter()
    creator = filters.AllValuesFilter()
    


    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']


f = AdvertisementFilter({'created_at_before': '2020-10-01'})
