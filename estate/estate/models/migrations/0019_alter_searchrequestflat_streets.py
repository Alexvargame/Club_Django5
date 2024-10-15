# Generated by Django 5.0.7 on 2024-08-30 08:58

import estate.models.search_requests
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0018_alter_searchrequestflat_cities_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchrequestflat',
            name='streets',
            field=models.JSONField(default=estate.models.search_requests.SearchRequestFlat.get_default_cities, null=True),
        ),
    ]