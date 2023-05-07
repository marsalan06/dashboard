from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Influencer, Business
from django.contrib.auth.models import User


class InfluencerForm(forms.ModelForm):

    def __init__(self, *args, users=None, **kwargs):
        super(InfluencerForm, self).__init__(*args, **kwargs)
        self.fields['user'] = forms.ModelChoiceField(queryset=users, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Influencer
        fields = ['name', 'state', 'city', 'zip_code', 'rank', 'status','user']
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
            'user': _('User')
        }


class BusinessForm(forms.ModelForm):

   
    class Meta:
        model = Business
        fields = ['name', 'contact_no', 'start_date', 'end_date', 'report_ready', 'influencer', 'type_of_business']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
            'reference_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'report_ready': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'influencer': forms.Select(attrs={'class': 'form-control'}),
            'type_of_business': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'name': _('Name'),
            'contact_no': _('Contact Number'),
            'start_date': _('Start Date'),
            'end_date': _('End Date'),
            'reference_no': _('Reference Number'),
            'report_ready': _('Report Ready'),
            'influencer': _('Influencer'),
            'type_of_business': _('Type Of Business')
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("Start date must be before end date.")

