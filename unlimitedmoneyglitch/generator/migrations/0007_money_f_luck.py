# Generated by Django 4.2.7 on 2024-01-07 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0006_leaderboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='money',
            name='f_luck',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
