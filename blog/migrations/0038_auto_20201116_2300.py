# Generated by Django 3.1.1 on 2020-11-16 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0037_auto_20201116_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='area_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(choices=[('ad', 'Abu Dhabi'), ('dxb', 'Dubai'), ('shj', 'Sharjah'), ('aj', 'Ajman'), ('rak', 'Ras Al Khaimah'), ('umq', 'Umm al Quwain'), ('fuj', 'Fujairah')], default='ad', max_length=6),
        ),
        migrations.DeleteModel(
            name='Area',
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]