# Generated by Django 3.0.3 on 2020-04-11 18:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asas', '0014_friend'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_post', models.ManyToManyField(related_name='mysate', to=settings.AUTH_USER_MODEL)),
                ('post', models.ManyToManyField(to='asas.Asas')),
            ],
        ),
    ]
