# Generated by Django 4.2.3 on 2023-08-01 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_project_group_alter_appuser_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='ciloxis_num',
            field=models.CharField(max_length=100),
        ),
    ]
