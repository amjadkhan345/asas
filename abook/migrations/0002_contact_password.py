# Generated by Django 3.0.3 on 2020-02-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='password',
            field=models.CharField(max_length=12, null='true'),
            preserve_default='true',
        ),
    ]
