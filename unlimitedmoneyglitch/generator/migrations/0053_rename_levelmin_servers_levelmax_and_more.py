# Generated by Django 4.2.7 on 2024-05-06 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0052_roundtime_seasontime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servers',
            old_name='levelmin',
            new_name='levelmax',
        ),
        migrations.RemoveField(
            model_name='game',
            name='roundcounter',
        ),
        migrations.RemoveField(
            model_name='game',
            name='roundseed',
        ),
        migrations.RemoveField(
            model_name='game',
            name='roundtime',
        ),
        migrations.RemoveField(
            model_name='game',
            name='roundtype',
        ),
        migrations.RemoveField(
            model_name='game',
            name='seasonseed',
        ),
        migrations.RemoveField(
            model_name='game',
            name='seasontime',
        ),
        migrations.RemoveField(
            model_name='game',
            name='seasontype',
        ),
        migrations.AddField(
            model_name='roundtime',
            name='maxleveldata',
            field=models.FloatField(default=80),
        ),
        migrations.AddField(
            model_name='seasontime',
            name='maxleveldata',
            field=models.FloatField(default=80),
        ),
        migrations.AddField(
            model_name='user',
            name='phase',
            field=models.FloatField(default=0),
        ),
    ]
