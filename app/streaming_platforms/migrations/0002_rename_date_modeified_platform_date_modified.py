# Generated by Django 4.0.10 on 2024-04-09 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_platforms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='platform',
            old_name='date_modeified',
            new_name='date_modified',
        ),
    ]
