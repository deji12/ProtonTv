# Generated by Django 4.2.1 on 2023-11-27 13:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('StreamsApp', '0003_alter_stream_stream_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='stream_id',
            field=models.CharField(default=uuid.UUID('33feb872-e0a4-4578-a6f8-a9c4ae5234e7'), max_length=225),
        ),
    ]
