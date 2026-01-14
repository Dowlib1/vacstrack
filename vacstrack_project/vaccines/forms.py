from django import forms
from .models import VaccineLog


class VaccineLogForm(forms.ModelForm):
    class Meta:
        model = VaccineLog
        fields = ['vaccine_type', 'date_administered', 'next_due_date', 'notes']
        widgets = {
            'date_administered': forms.DateInput(attrs={'type': 'date'}),
            'next_due_date': forms.DateInput(attrs={'type': 'date'}),

    def clean(self):
        cleaned = super().clean()
        start = cleaned.get('date_administered')
        next_due = cleaned.get('next_due_date')
        if start and next_due and next_due < start:
            raise forms.ValidationError("Next due date cannot be earlier than the date administered.")
        return cleaned
