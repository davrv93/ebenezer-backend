# Generated by Django 2.1.2 on 2018-10-05 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atencion', '0012_level_taxonomy'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]