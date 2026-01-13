from django.db import models
from django.contrib.auth.models import User


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

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vaccine_type = models.CharField(max_length=50, choices=VACCINE_TYPES)
    date_administered = models.DateField()
    next_due_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.vaccine_type} - {self.date_administered}" # Or  = f"{self.vaccine_type} administered on {self.date_administered}
