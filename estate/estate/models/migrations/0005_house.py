# Generated by Django 5.0.7 on 2024-08-14 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_alter_realestate_city_alter_realestate_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('realestate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='models.realestate')),
                ('area', models.FloatField()),
                ('type', models.CharField(choices=[('HOUSE', 'House'), ('HARF_HOUSE', 'Harf_house')], default='HOUSE', max_length=15)),
            ],
            bases=('models.realestate',),
        ),
    ]
