# Generated by Django 4.2.7 on 2024-01-17 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0016_playing_p_trades'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='p_pid',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
