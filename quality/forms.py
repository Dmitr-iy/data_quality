from django import forms
from .models import ConcentrateQuality


class ConcentrateQualityForm(forms.ModelForm):
    class Meta:
        model = ConcentrateQuality
        fields = '__all__'
