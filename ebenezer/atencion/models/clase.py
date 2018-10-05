from uuid import uuid4

from django.db import models

from .dominio import Dominio


class Clase(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid4, editable=False)
    dominio = models.ForeignKey(
        Dominio, related_name='clase_dominio_set', 
        db_column='dominio_id',
        blank=False,null=False,
        on_delete=models.CASCADE)
    nombre = models.CharField(
        unique=True, max_length=200,
        blank=False, null=False)
    descripcion = models.TextField(
        blank=True, null=True
    )
    
   
    class Meta:
        verbose_name = 'Clase'
        verbose_name_plural =  'Clase'
        default_permissions = ()
        permissions = (
            ('addd_clase',
             'Puede agregar Clase'),
            ('changed_clase',
             'Puede actualizar Clase'),
            ('deleted_clase',
             'Puede eliminar Clase'),
            ('listd_clase',
             'Puede listar Clase'),
            ('getd_clase',
             'Puede obtener Clase'),
        )
        db_table = 'atenciond_clase'

    def __str__(self):
        return self.nombre

