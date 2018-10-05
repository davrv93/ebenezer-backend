# Generated by Django 2.1.2 on 2018-10-05 13:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('atencion', '0007_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeOfLevel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'TypeOfLevel',
                'verbose_name': 'TypeOfLevel',
                'ordering': ('id',),
                'db_table': 'atencion_type_of_level',
            },
        ),
    ]
