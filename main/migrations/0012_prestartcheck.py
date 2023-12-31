# Generated by Django 4.2.3 on 2023-08-10 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_project_ciloxis_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrestartCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prestart_date', models.DateField(auto_now_add=True)),
                ('trained', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('sop_ra', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('test_tag', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('elect_lead', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('stop_button', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('guarding', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('interlock', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('dust_extract', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('hyd_pump', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('water_elect', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('water_level', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('air_pressure', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('seals', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('drainage', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('housekeeping', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('comments', models.CharField(max_length=500)),
                ('equip_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.equipment')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.appuser')),
            ],
        ),
    ]
