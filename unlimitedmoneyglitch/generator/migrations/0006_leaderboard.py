# Generated by Django 4.2.7 on 2024-01-07 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0005_game_optimization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ranking', models.PositiveIntegerField()),
                ('PNAME', models.CharField(max_length=16)),
                ('PLEVEL', models.PositiveIntegerField()),
            ],
        ),
    ]
