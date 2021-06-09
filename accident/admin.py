from django.contrib import admin

# Register your models here.
from accident.models import TypeAccident, Accident, Vehicule, Conducteur, Proprietaire, Permis, Victime, Temoin, \
    Declaration, Assurance, EtatDesLieux

admin.site.register(TypeAccident)
admin.site.register(Accident)
admin.site.register(Vehicule)
admin.site.register(Conducteur)
admin.site.register(Proprietaire)
admin.site.register(Permis)
admin.site.register(Victime)
admin.site.register(Temoin)
admin.site.register(Declaration)
admin.site.register(Assurance)
admin.site.register(EtatDesLieux)