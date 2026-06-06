from django import forms
from .models import People

def get_genders():
    return list(
        People.objects.exclude(gender=None)
        .values_list('gender', 'gender')
        .distinct()
        .order_by('gender')
    )

class searchForm(forms.Form):
    movieMinDate   = forms.DateField(required=True, label="Movies minimum release date")
    movieMaxDate   = forms.DateField(required=True, label="Movies maximum release date")
    planetDiameter = forms.IntegerField(required=True, label="Planet diameter greater than")
    characterGender = forms.ChoiceField(required=True, label="Character gender", choices=get_genders)