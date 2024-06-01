# Generated by Django 4.2.7 on 2024-01-10 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0013_friendrequests_friends_profile_alter_user_fakey_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='P_tmoney',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='p_acceptfriends',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='p_exp',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='p_forceluck',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='p_level',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='p_luck',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='p_messagesaccept',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='p_money',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='p_orders',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='p_playing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='p_storedluck',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='p_trades',
            field=models.BooleanField(default=True),
        ),
    ]
