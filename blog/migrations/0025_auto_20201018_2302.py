# Generated by Django 3.1.1 on 2020-10-18 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20201018_0741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='route',
            old_name='user',
            new_name='username',
        ),
    ]
