# Generated by Django 3.0.3 on 2020-04-21 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asas', '0026_auto_20200421_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asas',
            name='parent',
        ),
        migrations.AddField(
            model_name='asas',
            name='parent',
            field=models.ManyToManyField(null=True, related_name='_asas_parent_+', to='asas.Asas'),
        ),
    ]
