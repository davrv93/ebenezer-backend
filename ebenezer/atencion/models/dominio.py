from uuid import uuid4
from django.db import models


class Dominio(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid4, editable=False)
    nombre = models.CharField(
        unique=True, max_length=200,
        blank=False, null=False)
    descripcion = models.TextField(
        blank=True, null=True
    )
    
   
    class Meta:
        verbose_name = 'Dominio'
        verbose_name_plural =  'Dominio'
        default_permissions = ()
        permissions = (
            ('add_dominio',
             'Puede agregar Dominio'),
            ('change_dominio',
             'Puede actualizar Dominio'),
            ('delete_dominio',
             'Puede eliminar Dominio'),
            ('list_dominio',
             'Puede listar Dominio'),
            ('get_dominio',
             'Puede obtener Dominio'),
        )
        db_table = 'atencion_dominio'
        ordering=('id',)

    def __str__(self):
        return self.nombre

