# Generated by Django 4.2.7 on 2024-05-12 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0102_alter_servers_levelmax_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servers',
            name='max_players',
            field=models.PositiveIntegerField(default=100000),
        ),
    ]
