# Generated by Django 4.2.1 on 2023-12-11 20:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('StreamsApp', '0009_alter_stream_stream_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='stream_id',
            field=models.CharField(default=uuid.UUID('f3a398e3-fe78-4d02-9b7f-22fac3702e49'), max_length=225),
        ),
    ]
