from django.contrib import admin
from .models import Vaca, Produccion, EventoSanitario

@admin.register(Vaca)
class VacaAdmin(admin.ModelAdmin):
    list_display = ('numero_identificacion', 'nombre', 'raza', 'fecha_nacimiento', 'corral_actual')
    search_fields = ('numero_identificacion', 'nombre', 'raza')

@admin.register(Produccion)
class ProduccionAdmin(admin.ModelAdmin):
    list_display = ('vaca', 'fecha_registro', 'cantidad_litros', 'turno')

@admin.register(EventoSanitario)
class EventoSanitarioAdmin(admin.ModelAdmin):
    list_display = ('tipo_evento', 'fecha_evento', 'veterinario', 'costo', 'dias_retiro', 'notas')
