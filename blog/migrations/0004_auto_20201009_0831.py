# Generated by Django 3.1.1 on 2020-10-09 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201009_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='make_initial_location',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_number',
            field=models.IntegerField(),
        ),
    ]
