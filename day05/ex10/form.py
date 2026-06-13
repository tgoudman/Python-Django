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
    
    movieMinDate   = forms.DateTimeField(required=True, label="Movies minimum release date yyyy-mm-dd")
    movieMaxDate   = forms.DateTimeField(required=True, label="Movies maximum release date yyyy-mm-dd")
    planetDiameter = forms.IntegerField(required=True, label="Planet diameter greater than")
    characterGender = forms.ChoiceField(required=True, label="Character gender", choices=get_genders)