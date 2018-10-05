from uuid import uuid4

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from .taxonomy import Taxonomy
from .type_of_level import TypeOfLevel

class Level(MPTTModel):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid4, 
        editable=False)
    type_of_level = models.ForeignKey(
        TypeOfLevel, 
        related_name='level_type_of_level_set', 
        db_column='type_of_level_id',
        blank=False,null=False,
        on_delete=models.CASCADE)
    taxonomy = models.ForeignKey(
        Taxonomy,
        related_name='level_taxonomy_set',
        db_column='taxonomy_id',
        blank=True, null=True,
        on_delete=models.CASCADE
    )
    code = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    name = models.CharField(
        max_length=50, unique=True
    )
    description = models.TextField(
        null=True, blank=True
    )
    orden = models.IntegerField(
        blank=False,null=False
    )
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, 
        null=True, blank=True, 
        related_name='children'
    )

    class MPTTMeta:
        parent_attr='parent'
        order_insertion_by = ['orden']


    def __str__(self):
        return self.type_of_level.name + ': '+ self.name