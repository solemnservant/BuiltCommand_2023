# Generated by Django 2.2.24 on 2022-08-16 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20220816_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='safety_service',
            name='audit_schedule',
            field=models.DateTimeField(verbose_name='audit schedule'),
        ),
        migrations.AlterField(
            model_name='safety_service',
            name='training_schedule',
            field=models.DateTimeField(verbose_name='training schedule'),
        ),
    ]
