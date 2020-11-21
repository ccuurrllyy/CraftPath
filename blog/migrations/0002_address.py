# Generated by Django 3.1.1 on 2020-10-09 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=100)),
                ('area_name', models.CharField(max_length=200)),
                ('street_number', models.IntegerField(max_length=10, verbose_name={'placeholder': '12'})),
                ('street_name', models.CharField(max_length=30, verbose_name={'placeholder': 'Salam St'})),
                ('make_initial_location', models.BooleanField(verbose_name=False)),
            ],
        ),
    ]