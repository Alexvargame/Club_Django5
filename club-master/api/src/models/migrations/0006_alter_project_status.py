# Generated by Django 5.0.7 on 2024-08-04 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_project_categories_project_stacks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('OPEN', 'Открыт'), ('CLOSED', 'Закрыт'), ('STARTED', 'Стартовал'), ('BACKLOG', 'Backlog')], default='OPEN', max_length=15),
        ),
    ]
