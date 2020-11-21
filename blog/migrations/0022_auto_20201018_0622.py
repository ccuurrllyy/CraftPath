# Generated by Django 3.1.1 on 2020-10-18 02:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0021_auto_20201018_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='route',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
