# Generated by Django 4.2.3 on 2023-08-20 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_prestartcheck_hyd_oil_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestartcheck',
            name='fume_filter',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
    ]
