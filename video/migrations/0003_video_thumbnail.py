# Generated by Django 3.0.3 on 2020-05-15 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20200516_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='images'),
            preserve_default=False,
        ),
    ]
