# Generated by Django 4.2.7 on 2024-05-06 14:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0050_playing_p_server'),
    ]

    operations = [
        migrations.AddField(
            model_name='servers',
            name='levelmin',
            field=models.IntegerField(default=80, validators=[django.core.validators.MaxValueValidator(320), django.core.validators.MinValueValidator(1)]),
        ),
    ]
