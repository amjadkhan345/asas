# Generated by Django 3.0.3 on 2020-03-09 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abook', '0012_auto_20200309_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
