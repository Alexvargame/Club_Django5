# Generated by Django 5.0.7 on 2024-08-03 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]
