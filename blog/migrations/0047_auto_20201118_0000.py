# Generated by Django 3.1.1 on 2020-11-17 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0046_auto_20201117_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]