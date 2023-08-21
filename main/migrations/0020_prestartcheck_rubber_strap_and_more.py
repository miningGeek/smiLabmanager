# Generated by Django 4.2.3 on 2023-08-20 23:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0019_prestartcheck_fume_filter"),
    ]

    operations = [
        migrations.AddField(
            model_name="prestartcheck",
            name="rubber_strap",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="prestartcheck",
            name="air_pressure",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="prestartcheck",
            name="anti_slip",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="prestartcheck",
            name="drainage",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="prestartcheck",
            name="dust_extract",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="prestartcheck",
            name="elect_lead",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="prestartcheck",
            name="filter_mat",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="prestartcheck",
            name="fume_filter",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="prestartcheck",
            name="glass_bott",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="prestartcheck",
            name="guarding",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="prestartcheck",
            name="housekeeping",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="prestartcheck",
            name="hyd_oil_level",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="prestartcheck",
            name="hyd_pump",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="prestartcheck",
            name="interlock",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="prestartcheck",
            name="noise_baffles",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="prestartcheck",
            name="seals",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="prestartcheck",
            name="sop_ra",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")], max_length=10
            ),
        ),
        migrations.AlterField(
            model_name="prestartcheck",
            name="stop_button",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="prestartcheck",
            name="test_tag",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="prestartcheck",
            name="trained",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")], max_length=10
            ),
        ),
        migrations.AlterField(
            model_name="prestartcheck",
            name="water_elect",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="prestartcheck",
            name="water_level",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("NA", "NA")],
                max_length=10,
            ),
        ),
    ]