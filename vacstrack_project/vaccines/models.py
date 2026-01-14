from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError

class VaccineLog(models.Model):
    VACCINE_TYPES = [
        ('BCG', 'BCG'),
        ('HepB', 'Hepatitis B'),
        ('OPV', 'Oral Polio Vaccine'),
        ('DPT', 'Diphtheria, Pertussis, Tetanus'),
        ('Hib', 'Haemophilus influenzae type b'),
        ('PCV', 'Pneumococcal Conjugate'),
        ('Rotavirus', 'Rotavirus'),
        ('Measles', 'Measles / MMR'),
        ('Yellow Fever', 'Yellow Fever'),
        ('COVID-19', 'COVID-19'),
        ('Flu', 'Influenza'),
        ('HPV', 'Human Papillomavirus'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vaccine_logs')
    vaccine_type = models.CharField(max_length=50, choices=VACCINE_TYPES)
    date_administered = models.DateField()
    next_due_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_administered']
        constraints = [
            models.UniqueConstraint(fields=['user', 'vaccine_type', 'date_administered'], name='unique_vaccine_per_day')
        ]

    def clean(self):
        if self.next_due_date and self.next_due_date < self.date_administered:
            raise ValidationError("Next due date cannot be before the administered date.")

    def __str__(self):
        return f"{self.vaccine_type} on {self.date_administered} ({self.user.username})"
