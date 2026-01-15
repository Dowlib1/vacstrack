from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from .models import VaccineLog

class VaccineLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'vaccine_type', 'date_administered', 'next_due_date')
    list_filter = ('vaccine_type',)
    search_fields = ('user__username', 'notes')

# Register safely: if already registered, unregister then register with our admin
try:
    admin.site.register(VaccineLog, VaccineLogAdmin)
except AlreadyRegistered:
    admin.site.unregister(VaccineLog)
    admin.site.register(VaccineLog, VaccineLogAdmin)
