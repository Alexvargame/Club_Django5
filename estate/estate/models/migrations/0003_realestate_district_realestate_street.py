# Generated by Django 5.0.7 on 2024-08-13 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_realestate_city_district_street'),
    ]

    operations = [
        migrations.AddField(
            model_name='realestate',
            name='district',
            field=models.CharField(choices=[], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='realestate',
            name='street',
            field=models.CharField(choices=[], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
