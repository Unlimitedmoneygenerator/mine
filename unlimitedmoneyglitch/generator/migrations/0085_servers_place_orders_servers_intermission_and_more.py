# Generated by Django 4.2.7 on 2024-05-08 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0084_numbers_l_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='servers',
            name='PLACE_ORDERS',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='servers',
            name='intermission',
            field=models.PositiveIntegerField(default=48),
        ),
        migrations.AddField(
            model_name='servers',
            name='roundstarting',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='servers',
            name='takenleftorders',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='servers',
            name='intime',
            field=models.PositiveIntegerField(),
        ),
    ]
