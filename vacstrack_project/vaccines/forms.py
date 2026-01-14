from django import forms
from .models import VaccineLog


class VaccineLogForm(forms.ModelForm):
    class Meta:
        model = VaccineLog
        fields = ['vaccine_type', 'date_administered', 'next_due_date', 'notes']
        widgets = {
            'date_administered': forms.DateInput(attrs={'type': 'date'}),
            'next_due_date': forms.DateInput(attrs={'type': 'date'}),
        }
