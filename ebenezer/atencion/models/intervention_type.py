from uuid import uuid4
from django.db import models

class InterventionType(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid4, editable=False)
    name = models.CharField(
        unique=True, max_length=200,
        blank=False, null=False)
    description = models.TextField(
        blank=True, null=True
    )
    
   
    class Meta:
        verbose_name = 'InterventionType'
        verbose_name_plural =  'InterventionType'
        db_table = 'atencion_intervention_type'
        ordering=('id',)

    def __str__(self):
        return self.name
