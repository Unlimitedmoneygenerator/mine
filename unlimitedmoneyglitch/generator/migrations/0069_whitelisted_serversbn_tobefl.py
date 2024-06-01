# Generated by Django 4.2.7 on 2024-05-07 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0068_serversbn_s_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whitelisted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='serversbn',
            name='tobefl',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
