# Generated by Django 4.2.7 on 2024-01-08 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0008_modifiers_chumps_alter_money_f_luck'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=64)),
                ('PlayerName', models.CharField(max_length=16)),
                ('ordering', models.PositiveIntegerField()),
                ('Active', models.BooleanField()),
                ('Message', models.CharField(max_length=256)),
            ],
        ),
    ]
