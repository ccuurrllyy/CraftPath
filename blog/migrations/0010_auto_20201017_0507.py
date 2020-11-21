# Generated by Django 3.1.1 on 2020-10-17 01:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_auto_20201017_0501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='user',
        ),
        migrations.AddField(
            model_name='route',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
