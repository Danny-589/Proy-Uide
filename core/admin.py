from django.contrib import admin
from .models import Profile, Oferta, ClasificacionCandidato, Postulacion, Resena, OfertaFoto, ConfiguracionPlataforma

@admin.register(ConfiguracionPlataforma)
class ConfiguracionPlataformaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'requiere_verificacion_correo')

    
# Register other existing models for admin access
admin.site.register(Profile)
admin.site.register(Oferta)
admin.site.register(ClasificacionCandidato)
admin.site.register(Postulacion)
admin.site.register(Resena)
admin.site.register(OfertaFoto)
