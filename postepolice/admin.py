from django.contrib import admin

# Register your models here.
from postepolice.models import AgentPoste, Brigade, MainCourante, Registre

admin.site.register(AgentPoste)
admin.site.register(Brigade)
admin.site.register(MainCourante)
admin.site.register(Registre)