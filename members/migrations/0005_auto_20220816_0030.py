# Generated by Django 2.2.24 on 2022-08-16 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20220816_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='address2',
            field=models.CharField(default='Address_2', max_length=250, verbose_name='Address_2'),
        ),
    ]
