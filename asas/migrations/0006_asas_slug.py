# Generated by Django 3.0.3 on 2020-03-31 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asas', '0005_commint'),
    ]

    operations = [
        migrations.AddField(
            model_name='asas',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
