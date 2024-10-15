# Generated by Django 5.0.7 on 2024-09-14 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0027_alter_searchrequestflat_floor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30, verbose_name='Автор')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')),
                ('real_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.realestate', verbose_name='Объявление')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['created_at'],
            },
        ),
    ]
