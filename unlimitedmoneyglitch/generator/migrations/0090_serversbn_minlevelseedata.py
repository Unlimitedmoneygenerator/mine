# Generated by Django 4.2.7 on 2024-05-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0089_rename_amount_winners_p_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='serversbn',
            name='minlevelseedata',
            field=models.PositiveIntegerField(default=80),
        ),
    ]
