# Generated by Django 3.2.10 on 2021-12-20 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0022_delete_helprequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='text_content',
            new_name='text',
        ),
    ]
