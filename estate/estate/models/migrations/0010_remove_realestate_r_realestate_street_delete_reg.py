# Generated by Django 5.0.7 on 2024-08-15 08:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0009_realestate_r'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realestate',
            name='r',
        ),
        migrations.AddField(
            model_name='realestate',
            name='street',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='real_eatates', to='models.street'),
        ),
        migrations.DeleteModel(
            name='Reg',
        ),
    ]
