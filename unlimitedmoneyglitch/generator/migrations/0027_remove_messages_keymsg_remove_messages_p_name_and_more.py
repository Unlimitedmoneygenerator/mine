# Generated by Django 4.2.7 on 2024-01-22 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0026_user_acceptreq'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='keyMsg',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='p_name',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='sp_name',
        ),
        migrations.RemoveField(
            model_name='playing',
            name='P_tmoney',
        ),
        migrations.RemoveField(
            model_name='playing',
            name='p_currentrade',
        ),
        migrations.RemoveField(
            model_name='playing',
            name='p_exp',
        ),
        migrations.RemoveField(
            model_name='playing',
            name='p_id',
        ),
        migrations.RemoveField(
            model_name='playing',
            name='p_money',
        ),
        migrations.RemoveField(
            model_name='playing',
            name='p_trades',
        ),
        migrations.AlterField(
            model_name='messages',
            name='Msgcontent',
            field=models.CharField(max_length=10000000),
        ),
    ]
