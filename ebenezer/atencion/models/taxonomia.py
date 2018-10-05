from uuid import uuid4
from django.db import models

from .choices import TAXONOMIA_CHOICES

class Taxonomia(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid4, editable=False)
    nombre = models.CharField(
        unique=True, max_length=200,
        blank=False, null=False)
    abreviatura = models.CharField(
        unique=True, max_length=200,
        blank=False, null=False)
    codigo = models.CharField(
        unique=True, max_length=50,
        choices=TAXONOMIA_CHOICES,
        blank=False, null=False)
    descripcion = models.TextField(
        blank=True, null=True
    )
    
   
    class Meta:
        verbose_name = 'Taxonomia'
        verbose_name_plural =  'Taxonomia'
        default_permissions = ()
        permissions = (
            ('add_taxonomia',
             'Puede agregar Taxonomia'),
            ('change_taxonomia',
             'Puede actualizar Taxonomia'),
            ('delete_taxonomia',
             'Puede eliminar Taxonomia'),
            ('list_taxonomia',
             'Puede listar Taxonomia'),
            ('get_taxonomia',
             'Puede obtener Taxonomia'),
        )
        db_table = 'atencion_taxonomia'
        ordering=('id',)

    def __str__(self):
        return self.nombre

