# Generated by Django 5.0.7 on 2024-08-15 08:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='regi', to='real_estate.city')),
            ],
        ),
        migrations.AddField(
            model_name='realestate',
            name='regi',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='real_estates', to='real_estate.region'),
            preserve_default=False,
        ),
    ]
