# Generated by Django 4.2.7 on 2024-05-19 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0110_remove_numbers_l_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servers',
            name='intime',
            field=models.FloatField(default=2),
        ),
    ]