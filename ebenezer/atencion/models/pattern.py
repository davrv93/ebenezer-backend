from uuid import uuid4

from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Pattern(MPTTModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4, editable=False)
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children'
    )
    order = models.IntegerField(
        blank=False, null=False
    )
    name = models.CharField(
        unique=True, max_length=200,
        blank=False, null=False)
    description = models.TextField(
        blank=True, null=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Pattern'
        verbose_name_plural = 'Pattern'

        db_table = 'atencion_pattern'

    def __str__(self):
        return self.name

    class MPTTMeta:
        parent_attr = 'parent'
        order_insertion_by = ['order']
