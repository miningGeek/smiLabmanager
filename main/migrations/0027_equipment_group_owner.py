# Generated by Django 4.2.3 on 2023-08-31 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_prestartcheck_battery_condition_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='group_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.researchgroup'),
        ),
    ]
