# Generated by Django 4.2.3 on 2023-11-30 11:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_prestartcheck_cable_alter_sample_sample_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='request_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
