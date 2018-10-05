from uuid import uuid4
from django.db import models

from .choices import TAXONOMIA_CHOICES

class Taxonomy(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid4, editable=False)
    name = models.CharField(
        unique=True, max_length=200,
        blank=False, null=False)
    abbreviation = models.CharField(
        unique=True, max_length=200,
        blank=False, null=False)
    code = models.CharField(
        unique=True, max_length=50,
        choices=TAXONOMIA_CHOICES,
        blank=False, null=False)
    description = models.TextField(
        blank=True, null=True
    )
    
   
    class Meta:
        verbose_name = 'Taxonomy'
        verbose_name_plural =  'Taxonomy'
        default_permissions = ()
        permissions = (
            ('add_taxonomy',
             'Puede agregar Taxonomy'),
            ('change_taxonomy',
             'Puede actualizar Taxonomy'),
            ('delete_taxonomy',
             'Puede eliminar Taxonomy'),
            ('list_taxonomy',
             'Puede listar Taxonomy'),
            ('get_taxonomy',
             'Puede obtener Taxonomy'),
        )
        db_table = 'atencion_taxonomy'
        ordering=('id',)

    def __str__(self):
        return self.name

