from uuid import uuid4

from django.db import models

from .related_factor import RelatedFactor


class DiagnosticTag(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4, editable=False)

    related_factor = models.ManyToManyField(
        RelatedFactor,
        blank=True,
        db_table='atencion_diag_tag_related',
        related_name='diag_tag_related_set'
    )
    code = models.CharField(
        max_length=50,
        blank=True, null=True,
        unique=True
    )
    order = models.IntegerField(
        blank=True, null=True
    )
    name = models.CharField(
        unique=True, max_length=200,
        blank=False, null=False)
    description = models.TextField(
        blank=True, null=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'DiagnosticTag'
        verbose_name_plural = 'DiagnosticTag'

        db_table = 'atencion_diagnostic_tag'

    def __str__(self):
        return self.name
