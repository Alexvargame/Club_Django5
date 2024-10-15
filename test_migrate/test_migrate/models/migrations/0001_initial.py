# Generated by Django 5.0.7 on 2024-08-15 11:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_object', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('site_link', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('square', models.FloatField(default=1.0)),
                ('price', models.DecimalField(decimal_places=2, default=1.0, max_digits=10)),
                ('number_address_building', models.CharField(default=1, max_length=5)),
                ('number_address_appart', models.CharField(default=1, max_length=5)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='real_estates', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='districts', to='models.city')),
            ],
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('realestate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='models.realestate')),
                ('floor', models.IntegerField(default=1)),
                ('number_of_storeys', models.IntegerField(default=1)),
                ('type', models.CharField(choices=[('FLAT', 'Flat'), ('SMART_FLAT', 'Smart_flat')], default='FLAT', max_length=15)),
            ],
            bases=('models.realestate',),
        ),
        migrations.AddField(
            model_name='realestate',
            name='district',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='real_estates', to='models.district'),
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='streets', to='models.city')),
            ],
        ),
    ]