from uuid import uuid4

from django.db import models


class Shifts(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4, editable=False)

    name = models.CharField(
        max_length=200,
        blank=False, null=False)

    start = models.TimeField(
        blank=False, null=False

    )

    end = models.TimeField(
        blank=False, null=False
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Shifts'
        verbose_name_plural = 'Shifts'

        db_table = 'config_shifts'

    def __str__(self):
        return self.name
