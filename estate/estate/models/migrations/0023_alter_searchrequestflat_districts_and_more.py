# Generated by Django 5.0.7 on 2024-08-30 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0022_alter_searchrequestflat_cities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchrequestflat',
            name='districts',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='searchrequestflat',
            name='streets',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
