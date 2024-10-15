# Generated by Django 5.0.7 on 2024-08-14 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_realestate_district_realestate_street'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestate',
            name='city',
            field=models.CharField(choices=[('1', 'Харьков')], max_length=100),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='description',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='district',
            field=models.CharField(choices=[('1', 'Харьков:ГСВ')], max_length=100),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='street',
            field=models.CharField(choices=[('1', 'Харьков:Юрия Гагарина, проспект')], max_length=100),
        ),
    ]
