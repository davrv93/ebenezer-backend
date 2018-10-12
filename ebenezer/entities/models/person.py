from uuid import uuid4

from django.db import models

from .related_factor import RelatedFactor

sex_choices = (
    ('M', 'Masculino'),
    ('F', 'Femenino')
)


class Person(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4, editable=False)

    name = models.CharField(
        unique=True, max_length=200,
        blank=False, null=False)

    sex = models.CharField(
        blank=True, null=True,
        choices=sex_choices
    )

    birth_date = models.DateField(
        blank=True, null=True
    )

    phone = models.TextField(
        blank=True, null=True
    )

    address = models.TextField(
        blank=True, null=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Person'
        verbose_name_plural = 'Person'

        db_table = 'entities_person'

    def __str__(self):
        return self.name
