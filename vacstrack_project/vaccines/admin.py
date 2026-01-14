from django.contrib import admin
from .models import VaccineLog

admin.site.register(VaccineLog)

@admin.register(VaccineLog)
class VaccineLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'vaccine_type', 'date_administered', 'next_due_date')
    list_filter = ('vaccine_type',)
    search_fields = ('user__username', 'notes')
