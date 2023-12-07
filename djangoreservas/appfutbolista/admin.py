from django.contrib import admin
from .models import Mascota,Dueño
from django.contrib.auth.models import Permission

# Register your models here.

admin.site.register(Permission)

class MascotaAdmin(admin.ModelAdmin):
    list_display=['nombre','edad','fecha_de_nacimiento','sexo','dueño']
admin.site.register(Mascota,MascotaAdmin)

class DueñoAdmin(admin.ModelAdmin):
    list_display=['apellido_paterno','apellido_materno','nombres','fecha_nacimiento','motivo_de_visita']
admin.site.register(Dueño,DueñoAdmin)
