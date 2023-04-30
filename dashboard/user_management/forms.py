from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Influencer

class InfluencerForm(forms.ModelForm):
    class Meta:
        model = Influencer
        fields = ['name', 'state', 'city', 'zip_code', 'rank', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'rank': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': _('Name'),
            'state': _('State'),
            'city': _('City'),
            'zip_code': _('Zip Code'),
            'rank': _('Rank'),
            'status': _('Status'),
        }
