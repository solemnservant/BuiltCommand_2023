# Generated by Django 2.2.24 on 2023-02-11 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_auto_20220816_2257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='text',
            new_name='address',
        ),
        migrations.AlterField(
            model_name='member',
            name='text',
            field=models.CharField(default='Office Name', max_length=200, verbose_name='Office Name'),
        ),
    ]
