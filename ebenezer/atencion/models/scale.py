from uuid import uuid4
from django.db import models

class Scale(models.Model):
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
        verbose_name = 'Scale'
        verbose_name_plural =  'Scale'
        db_table = 'atencion_scale'
        ordering=('id',)

    def __str__(self):
        return self.name
