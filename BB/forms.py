from django import forms
from .models import BloodInventory, Donor, Request

class DonorForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # Allow user input for date
    class Meta:
        model = Donor
        fields = '__all__'

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'


class BloodInventoryForm(forms.ModelForm):
    class Meta:
        model = BloodInventory
        fields = ['blood_type', 'units']