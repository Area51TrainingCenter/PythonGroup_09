from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(
        max_length=20,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.nombre


class Mocion(models.Model):
    nombre = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )

    # imagenes

    contenido = models.TextField(
        blank=False,
        null=False
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    presupuesto = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        blank=True,
        null=True
    )

    estado = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        default='propuesta',
        choices=(
            ('propuesta', 'Propuesta de usuario'),
            ('discusion', 'En discusión del congreso'),
            ('aprobado_p', 'Propuesta aprobada'),
            ('aprobado_d', 'Discusión aprobada'),
            ('rechazado_p', 'Propuesta rechazada'),
            ('rechazado_d', 'Discusión rechazada'),
        )
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Moción'
        verbose_name_plural = 'Mociones'
