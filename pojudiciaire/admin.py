from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.auth.models import Group
# Register your models here.
from .models import Saisine, Crime, Audition, TypeInfraction

admin.site.site_header = 'COMMISSARIAT CENTRAL DE KAOLACK'



# Apply summernote to all TextField in model.
class SaisineAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
admin.site.register(Crime)
admin.site.register(Audition)
admin.site.register(TypeInfraction)
admin.site.register(Saisine, SaisineAdmin)