from uuid import uuid4

from django.db import models

from .diagnostic_tag import DiagnosticTag

from .pattern import Pattern


class DefiningCharacteristic(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4, editable=False)

    diagnostic_tag = models.ManyToManyField(
        DiagnosticTag,
        blank=True,
        db_table='atencion_def_char_diag_tag',
        related_name='def_char_diag_tag_set'
    )

    pattern = models.ManyToManyField(
        Pattern,
        blank=True,
        db_table='atencion_def_char_pattern',
        related_name='def_char_pattern_set'
    )

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
        verbose_name = 'DefiningCharacteristic'
        verbose_name_plural = 'DefiningCharacteristic'

        db_table = 'atencion_def_char'

    def __str__(self):
        return self.name
