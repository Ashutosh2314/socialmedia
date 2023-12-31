# Generated by Django 3.2.10 on 2021-12-16 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_delete_kcalamount'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirectMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.TextField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dm_reply_set', to='users.directmessage')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dm_recipient_set', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dm_sender_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
