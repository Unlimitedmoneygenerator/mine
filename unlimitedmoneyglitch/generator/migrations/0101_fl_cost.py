# Generated by Django 4.2.7 on 2024-05-11 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0100_alter_servers_intime_alter_servers_players_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fl',
            name='cost',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
