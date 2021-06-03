from django.contrib import admin

# Register your models here.
from accident.models import TypeAccident, Accident

admin.site.register(TypeAccident)
admin.site.register(Accident)