# Generated by Django 4.2.7 on 2024-01-12 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0014_alter_user_p_tmoney_alter_user_p_acceptfriends_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playing',
            options={},
        ),
        migrations.RemoveField(
            model_name='playing',
            name='p_acceptfriends',
        ),
        migrations.RemoveField(
            model_name='playing',
            name='p_banned',
        ),
        migrations.RemoveField(
            model_name='playing',
            name='p_forceluck',
        ),
        migrations.RemoveField(
            model_name='playing',
            name='p_friends',
        ),
        migrations.RemoveField(
            model_name='playing',
            name='p_inventory',
        ),
        migrations.RemoveField(
            model_name='playing',
            name='p_messages',
        ),
        migrations.RemoveField(
            model_name='playing',
            name='p_messagesaccept',
        ),
        migrations.RemoveField(
            model_name='playing',
            name='p_slot',
        ),
        migrations.RemoveField(
            model_name='playing',
            name='p_storedluck',
        ),
        migrations.RemoveField(
            model_name='playing',
            name='p_trades',
        ),
    ]
