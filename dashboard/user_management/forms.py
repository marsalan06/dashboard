from typing import Any, Dict
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Influencer, Business
from django.contrib.auth.models import User


class InfluencerForm(forms.ModelForm):

    def __init__(self, *args, users=None, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
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
            # 'user': _('User'),
            # 'business_association': _('Business Association')
            
        }
    def clean(self) -> Dict[str, Any]:
        if Influencer.objects.filter(user_id=self.user.id).exists():
            self.add_error(None,f"A user {self.user} with an associated influencer cannot create an other influencer account.")
        return super().clean()


class BusinessForm(forms.ModelForm):

   
    class Meta:
        model = Business
        fields = ['name', 'contact_no', 'start_date', 'end_date', 'report_ready', 'type_of_business']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
            'reference_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'report_ready': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            # 'influencer_association': forms.Select(attrs={'class': 'form-control'}),
            'type_of_business': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'name': _('Name'),
            'contact_no': _('Contact Number'),
            'start_date': _('Start Date'),
            'end_date': _('End Date'),
            'reference_no': _('Reference Number'),
            'report_ready': _('Report Ready'),
            # 'influencer_association': _('Influencer'),
            'type_of_business': _('Type Of Business')
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        print(self.user.id)
        super().__init__(*args, **kwargs)
        
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("Start date must be before end date.")

        
        if Influencer.objects.filter(user_id=self.user.id).exists():
            self.add_error(None,f"A user {self.user} with an associated influencer cannot create a business account.")
            # raise forms.ValidationError("A user with an associated influencer cannot create a business account.")

        return cleaned_data


