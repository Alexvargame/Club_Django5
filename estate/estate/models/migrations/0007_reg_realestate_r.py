# Generated by Django 5.0.7 on 2024-08-15 08:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0006_remove_realestate_city_remove_realestate_street_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='realestate',
            name='r',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='re', to='models.reg'),
            preserve_default=False,
        ),
    ]
