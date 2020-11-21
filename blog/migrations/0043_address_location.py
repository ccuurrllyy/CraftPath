# Generated by Django 3.1.1 on 2020-11-17 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0042_auto_20201117_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='location',
            field=models.CharField(choices=[('aau', 'Al Ain University'), ('dalma', 'Dalma Mall'), ('mazyad', 'Mazyad Mall'), ('deer', 'Deerfield Mall'), ('yas', 'Yas Mall'), ('marina', 'Marina Mall'), ('khaldiya', 'Khalidiya Mall'), ('abudhabi', 'Abu Dhabi Mall'), ('wahda', 'Al Wahda Mall'), ('miraj', 'Miraj Restaurant'), ('havana', 'Havana Cafe'), ('pacifiko', 'Pacifiko Tiki Lounge'), ('ferrari', 'Ferrari World'), ('hosn', 'Qasr al hosn'), ('emirates', 'Emirates Palace'), ('louvre', 'Louvre Museum'), ('chricket', 'Sheikh Zayed Cricket Stadium'), ('yww', 'Yas Water World'), ('masdar', 'Masdar City'), ('ferrari', 'Ferrari World'), ('zaya', 'Zaya Nuraie Island')], default='NULL', max_length=30),
        ),
    ]
