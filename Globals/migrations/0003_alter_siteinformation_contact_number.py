# Generated by Django 4.2.1 on 2023-12-30 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Globals', '0002_siteinformation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteinformation',
            name='contact_number',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
