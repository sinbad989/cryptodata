from django import forms
import django_filters
from .models import Data

class DataFilter(django_filters.FilterSet):
    TYPE = (
        (0,'Coin'),
        (1,'Token'),
    )

    name = django_filters.CharFilter(lookup_expr='icontains')
    symbol = django_filters.CharFilter(lookup_expr='icontains')
    cryptype = django_filters.ChoiceFilter(choices = TYPE,widget=forms.CheckboxSelectMultiple)

    class Meta:
        model  = Data
        fields  = ['name','cryptype','symbol','algorithm','proof']