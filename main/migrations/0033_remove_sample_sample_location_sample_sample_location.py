# Generated by Django 4.2.3 on 2023-09-16 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_sample_client_sample_client_contact_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='sample_location',
        ),
        migrations.AddField(
            model_name='sample',
            name='sample_location',
            field=models.ManyToManyField(blank=True, null=True, to='main.location'),
        ),
    ]
