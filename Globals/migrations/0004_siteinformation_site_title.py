# Generated by Django 4.2.1 on 2023-12-30 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Globals', '0003_alter_siteinformation_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinformation',
            name='site_title',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
