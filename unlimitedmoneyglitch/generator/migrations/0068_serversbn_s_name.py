# Generated by Django 4.2.7 on 2024-05-07 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0067_captureadmin_paymenthelp_serversbn_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='serversbn',
            name='s_name',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
