# Generated by Django 4.2.3 on 2023-09-07 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_appuser_ute_auth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='client_concat_name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='description',
        ),
        migrations.RemoveField(
            model_name='client',
            name='site_contact_email',
        ),
        migrations.RemoveField(
            model_name='client',
            name='site_contact_name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='site_name',
        ),
    ]