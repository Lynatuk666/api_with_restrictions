from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django_filters import rest_framework as filters, DateFromToRangeFilter

from advertisements.models import Advertisement



class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at  = DateFromToRangeFilter()
    creator = filters.ModelChoiceFilter()

    class Meta:
        model = Advertisement
        fields = ('created_at',)