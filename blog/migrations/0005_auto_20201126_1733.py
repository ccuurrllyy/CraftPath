# Generated by Django 2.0.13 on 2020-11-26 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201126_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='blog.Route'),
        ),
    ]