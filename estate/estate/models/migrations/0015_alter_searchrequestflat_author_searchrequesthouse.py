# Generated by Django 5.0.7 on 2024-08-29 07:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0014_searchrequestflat_rooms'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchrequestflat',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='search_flat_requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='SearchRequestHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('square', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('districts', models.CharField(max_length=500)),
                ('cities', models.CharField(max_length=500)),
                ('streets', models.CharField(max_length=500)),
                ('rooms', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='search_house_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]