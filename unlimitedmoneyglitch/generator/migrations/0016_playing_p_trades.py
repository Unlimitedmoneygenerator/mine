# Generated by Django 4.2.7 on 2024-01-12 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0015_alter_playing_options_remove_playing_p_acceptfriends_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='playing',
            name='p_trades',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]