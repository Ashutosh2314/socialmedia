# Generated by Django 3.2.8 on 2021-11-01 20:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communities', '0002_remove_post_responded_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='responded_users',
            field=models.ManyToManyField(related_name='responded_users_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
