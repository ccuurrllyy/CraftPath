# Generated by Django 3.1.1 on 2020-11-16 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0035_auto_20201115_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='street_name',
        ),
        migrations.RemoveField(
            model_name='address',
            name='street_number',
        ),
    ]