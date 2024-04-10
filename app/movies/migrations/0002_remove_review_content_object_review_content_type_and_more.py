# Generated by Django 4.0.10 on 2024-04-09 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='content_object',
        ),
        migrations.AddField(
            model_name='review',
            name='content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
