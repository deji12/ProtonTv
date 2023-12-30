# Generated by Django 4.2.1 on 2023-12-30 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('Globals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(blank=True, max_length=225, null=True)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_number', models.EmailField(blank=True, max_length=254, null=True)),
                ('footer_message', models.TextField(blank=True, null=True)),
                ('contact_page_message', models.TextField(blank=True, null=True)),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
        ),
    ]
