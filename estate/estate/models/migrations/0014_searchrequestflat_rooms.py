# Generated by Django 5.0.7 on 2024-08-27 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0013_flat_rooms_house_rooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchrequestflat',
            name='rooms',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
