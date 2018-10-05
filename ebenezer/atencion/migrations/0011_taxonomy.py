# Generated by Django 2.1.2 on 2018-10-05 17:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('atencion', '0010_level_orden'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taxonomy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('abbreviation', models.CharField(max_length=200, unique=True)),
                ('code', models.CharField(choices=[('NIC', 'NIC'), ('NOC', 'NOC')], max_length=50, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Taxonomy',
                'permissions': (('add_taxonomy', 'Puede agregar Taxonomy'), ('change_taxonomy', 'Puede actualizar Taxonomy'), ('delete_taxonomy', 'Puede eliminar Taxonomy'), ('list_taxonomy', 'Puede listar Taxonomy'), ('get_taxonomy', 'Puede obtener Taxonomy')),
                'default_permissions': (),
                'db_table': 'atencion_taxonomy',
                'verbose_name': 'Taxonomy',
                'ordering': ('id',),
            },
        ),
    ]
