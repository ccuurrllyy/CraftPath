# Generated by Django 3.1.1 on 2020-11-15 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_address_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='street_number',
            field=models.CharField(max_length=30),
        ),
    ]
