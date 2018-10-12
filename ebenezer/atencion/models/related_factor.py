from uuid import uuid4

from django.db import models


class RelatedFactor(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4, editable=False)
    code = models.CharField(
        max_length=50,
        blank=True, null=True,
        unique=True
    )
    name = models.CharField(
        unique=True, max_length=200,
        blank=False, null=False)
    description = models.TextField(
        blank=True, null=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'RelatedFactor'
        verbose_name_plural = 'RelatedFactor'

        db_table = 'atencion_related_factor'

    def __str__(self):
        return self.name
