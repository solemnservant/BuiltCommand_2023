# Generated by Django 2.2.24 on 2022-08-16 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='address2',
            field=models.CharField(default='Address', max_length=250, verbose_name='Address 2'),
        ),
    ]
