# Generated by Django 5.0.7 on 2024-08-15 08:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0004_realestate_re'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realestate',
            name='re',
        ),
        migrations.AddField(
            model_name='realestate',
            name='street',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='real_estates', to='real_estate.street'),
            preserve_default=False,
        ),
    ]
