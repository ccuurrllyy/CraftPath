# Generated by Django 3.1.3 on 2020-11-20 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0050_auto_20201121_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='latitude',
            field=models.FloatField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='longitude',
            field=models.FloatField(blank=True, default=None, max_length=30, null=True),
        ),
    ]
