# Generated by Django 4.2.3 on 2023-08-11 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_equipmentgroup_equip_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='equip_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.equipmentgroup'),
        ),
    ]
