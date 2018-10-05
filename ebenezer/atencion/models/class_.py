from uuid import uuid4

from django.db import models

from .domain import Domain


class Class(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid4, editable=False)
    domain = models.ForeignKey(
        Domain, related_name='class_dominio_set', 
        db_column='domain_id',
        blank=False,null=False,
        on_delete=models.CASCADE)
    name = models.CharField(
        unique=True, max_length=200,
        blank=False, null=False)
    description = models.TextField(
        blank=True, null=True
    )
    
   
    class Meta:
        verbose_name = 'Class'
        verbose_name_plural =  'Class'
       
        db_table = 'atenciond_class'

    def __str__(self):
        return self.name

