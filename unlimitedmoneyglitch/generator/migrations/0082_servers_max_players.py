# Generated by Django 4.2.7 on 2024-05-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0081_servers_players'),
    ]

    operations = [
        migrations.AddField(
            model_name='servers',
            name='max_players',
            field=models.PositiveIntegerField(default=10000),
        ),
    ]
