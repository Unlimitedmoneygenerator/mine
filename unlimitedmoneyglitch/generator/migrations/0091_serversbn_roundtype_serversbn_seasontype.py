# Generated by Django 4.2.7 on 2024-05-09 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0090_serversbn_minlevelseedata'),
    ]

    operations = [
        migrations.AddField(
            model_name='serversbn',
            name='roundtype',
            field=models.CharField(default='normal', max_length=64),
        ),
        migrations.AddField(
            model_name='serversbn',
            name='seasontype',
            field=models.CharField(default='normal', max_length=64),
        ),
    ]
