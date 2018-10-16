# Generated by Django 2.1.2 on 2018-10-11 04:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('atencion', '0014_interventiontype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'atencion_pattern',
                'verbose_name': 'Pattern',
                'verbose_name_plural': 'Pattern',
            },
        ),
    ]