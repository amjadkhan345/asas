# Generated by Django 3.0.3 on 2020-04-04 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asas', '0012_remove_commint_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commint',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='commint',
            old_name='user_id',
            new_name='user',
        ),
    ]
