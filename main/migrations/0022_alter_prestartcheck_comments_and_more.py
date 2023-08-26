# Generated by Django 4.2.3 on 2023-08-26 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_appuser_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestartcheck',
            name='comments',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='prestartcheck',
            name='elect_lead',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='prestartcheck',
            name='sop_ra',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='prestartcheck',
            name='test_tag',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='prestartcheck',
            name='trained',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
    ]