# Generated by Django 4.2.7 on 2024-05-19 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0109_angels'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='numbers',
            name='L_name',
        ),
    ]
