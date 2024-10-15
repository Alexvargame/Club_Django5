# Generated by Django 5.0.7 on 2024-08-03 17:28

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
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=5000)),
                ('repo_link', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('CLOSED', 'Closed'), ('STARTED', 'Started'), ('BACKLOG', 'Backlog')], default='OPEN', max_length=15)),
                ('author_role', models.CharField(choices=[('BACKEND', 'Backend'), ('FRONTEND', 'Frontend'), ('FULLSTACK', 'Fullstack'), ('DESIGN', 'Design'), ('DEVOPS', 'Devops'), ('QA', 'QA'), ('PM', 'PM'), ('OTHER', 'Other')], default='BACKEND', max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField(null=True)),
                ('closed_at', models.DateTimeField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]