from django.contrib import admin
from .models import Patient, Suivipatient
from .forms import SuivipatientAdminForm


# Register your models here.
# Filtrer | barre de recherche
class PatientAdmin(admin.ModelAdmin):
    search_fields = ('code_patient',)
    list_display = ('code_patient', 'date_admission', 'pathologie', 'centre_sante')
    list_filter = ('centre_sante',)

class SuivipatientatientAdmin(admin.ModelAdmin):
    form = SuivipatientAdminForm
    search_fields = ('code_patient',)
    list_display = ('code_patient', 'date_derniere_visite', 'dotation')
    list_filter = ('date_derniere_visite',)
    autocomplete_fields = ('code_patient',)

class SuivipatientAdmin2(admin.ModelAdmin):
    form = SuivipatientAdminForm

admin.site.register(Patient, PatientAdmin)
admin.site.register(Suivipatient,SuivipatientatientAdmin)
#admin.site.register(Suivipatient, SuivipatientAdmin2)

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _("Projet SME Bouake")
admin.site.site_title = _("Interface utilisateur DB")
admin.site.index_title = _("Welcome to SME Project")
