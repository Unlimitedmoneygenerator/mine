# Generated by Django 4.2.7 on 2024-02-25 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0038_alter_game_minleveldata_alter_game_roundcounter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverside',
            name='PLAYERAMOUNT',
            field=models.PositiveIntegerField(default=10000),
            preserve_default=False,
        ),
    ]
