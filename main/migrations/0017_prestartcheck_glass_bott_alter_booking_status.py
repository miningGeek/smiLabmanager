# Generated by Django 4.2.3 on 2023-08-20 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_prestartcheck_anti_slip_prestartcheck_filter_mat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestartcheck',
            name='glass_bott',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Completed', 'Completed'), ('Rejected', 'Rejected'), ('Cancelled', 'Cancelled'), ('Pending', 'Pending')], default='Pending', max_length=50),
        ),
    ]
