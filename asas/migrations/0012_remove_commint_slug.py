# Generated by Django 3.0.3 on 2020-04-01 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asas', '0011_auto_20200401_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commint',
            name='slug',
        ),
    ]
