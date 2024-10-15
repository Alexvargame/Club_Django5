# Generated by Django 5.0.7 on 2024-08-21 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0007_alter_category_description_alter_stack_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('INTERN', 'Стажер'), ('JUNIOR', 'Junior'), ('JUNIOR_PLUS', 'Junior+'), ('MIDDLE', 'Middle'), ('MIDDLE_PLUS', 'Middle+'), ('SENIOR', 'Senior'), ('SENIOR_PLUS', 'Senior+')], default='JUNIOR', max_length=35)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('closed_at', models.DateTimeField(blank=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_vacancies', to='models.project')),
                ('stack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tack_vacancies', to='models.stack')),
            ],
        ),
    ]