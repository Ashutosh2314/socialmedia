# Generated by Django 3.2.6 on 2021-12-04 22:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communities', '0019_requestforhelp_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RequestForHelp',
            new_name='HelpRequest',
        ),
    ]
