from django.db import models

# =-=-=-=-=-
# MODELO: VACA
# =-=-=-=-=-
class Vaca(models.Model):
    numero_identificacion = models.CharField(max_length=20, unique=True, verbose_name="Número de Identificación") 
    nombre = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nombre de la Vaca")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    raza = models.CharField(max_length=50, verbose_name="Raza") 
    estado_reproductivo = models.CharField(max_length=50, default="No gestante", verbose_name="Estado Reproductivo")
    peso_kg = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Peso (kg)")
    corral_actual = models.CharField(max_length=30, verbose_name="Corral Actual")
    notas = models.TextField(blank=True, verbose_name="Notas de la Vaca") 

    def __str__(self):
        return f"{self.nombre or 'Vaca'} {self.numero_identificacion}"

# =-=-=-=-=-
# MODELO: PRODUCCION (Relación 1:N con Vaca)
# =-=-=-=-=-
class Produccion(models.Model):
    vaca = models.ForeignKey(Vaca, on_delete=models.CASCADE, related_name='producciones', verbose_name="Vaca asociada") 
    fecha_registro = models.DateField(verbose_name="Fecha de Registro")
    cantidad_litros = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Cantidad (Litros)")
    turno = models.CharField(max_length=20, verbose_name="Turno")
    calidad = models.CharField(max_length=100, verbose_name="Detalles de Calidad") 
    empleado_registro = models.CharField(max_length=100, verbose_name="Empleado que Registra")
    equipo_usado = models.CharField(max_length=100, blank=True, verbose_name="Equipo Usado")

    def __str__(self):
        return f"Prod. {self.cantidad_litros}L de {self.vaca.numero_identificacion}"

# =-=-=-=-=-=-=
# MODELO: EVENTO SANITARIO (Relación 1:N con Vaca)
# =-=-=-=-=-=-=
class EventoSanitario(models.Model):
    vaca = models.ForeignKey(Vaca, on_delete=models.CASCADE, related_name='eventos_sanitarios', verbose_name="Vaca asociada")
    tipo_evento = models.CharField(max_length=100, verbose_name="Tipo de Evento")
    fecha_evento = models.DateField(verbose_name="Fecha del Evento")
    veterinario = models.CharField(max_length=100, verbose_name="Veterinario Responsable")
    descripcion = models.TextField(blank=True, verbose_name="Descripción del Evento")
    costo = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Costo del Evento")
    dias_retiro = models.IntegerField(default=0, verbose_name="Días de Retiro")
    notas = models.TextField(blank=True, verbose_name="Notas adicionales")  # ← agregado

    def __str__(self):
        return f"{self.tipo_evento} - {self.vaca.nombre}"

