# Generated by Django 4.2.7 on 2024-05-10 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0098_fl_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='black',
            name='time',
            field=models.PositiveIntegerField(default=60),
        ),
    ]
