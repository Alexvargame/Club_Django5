# Generated by Django 5.0.7 on 2024-08-26 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0011_searchrequestflat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searchrequestflat',
            old_name='city',
            new_name='cities',
        ),
        migrations.RenameField(
            model_name='searchrequestflat',
            old_name='district',
            new_name='districts',
        ),
        migrations.RenameField(
            model_name='searchrequestflat',
            old_name='street',
            new_name='streets',
        ),
    ]