# Generated by Django 4.2.7 on 2024-02-07 19:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0033_remove_ticket_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
