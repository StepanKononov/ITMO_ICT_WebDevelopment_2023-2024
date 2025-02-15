from django import forms

from .models import CarOwner, Car


class CarOwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = ['first_name', 'last_name', 'birth_date', 'passport_number', 'home_address', 'nationality']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['registration_number', 'brand', 'model', 'color']
