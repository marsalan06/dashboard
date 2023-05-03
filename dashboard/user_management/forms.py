from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Influencer, Business

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


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'contact_no', 'start_date', 'end_date', 'report_ready', 'influencer']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
            'reference_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'report_ready': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'influencer': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': _('Name'),
            'contact_no': _('Contact Number'),
            'start_date': _('Start Date'),
            'end_date': _('End Date'),
            'reference_no': _('Reference Number'),
            'report_ready': _('Report Ready'),
            'influencer': _('Influencer'),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("Start date must be before end date.")

    # def save(self, user, commit=True):
    #     business = super().save(commit=False)
    #     business.user = user
    #     if commit:
    #         business.save()
    #         self.save_m2m()
    #     return business
