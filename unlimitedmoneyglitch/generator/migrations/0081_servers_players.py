# Generated by Django 4.2.7 on 2024-05-08 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0080_servers_planet'),
    ]

    operations = [
        migrations.AddField(
            model_name='servers',
            name='players',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
