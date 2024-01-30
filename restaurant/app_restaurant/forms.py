from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'specialization', 'address', 'website', 'phone']

class SearchForm(forms.Form):
    specialization = forms.CharField(max_length=100, required=False)