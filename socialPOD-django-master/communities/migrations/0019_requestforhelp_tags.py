# Generated by Django 3.2.9 on 2021-12-01 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0018_auto_20211201_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestforhelp',
            name='tags',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
