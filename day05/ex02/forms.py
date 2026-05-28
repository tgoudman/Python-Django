from django import forms

class resetDataBase(forms.Form):
	confirm = forms.BooleanField(required=True)