# Generated by Django 4.2.7 on 2024-05-15 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0106_serversbn_incentive'),
    ]

    operations = [
        migrations.CreateModel(
            name='TRANSFERSDEPOSIT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=128)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='WITHDRAWALDEPOSIT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=128)),
                ('amount', models.FloatField()),
            ],
        ),
    ]