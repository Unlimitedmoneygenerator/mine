# Generated by Django 4.2.7 on 2024-01-28 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0029_keys_p_id_usedkeys_p_id_alter_usedkeys_p_used'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeysBANNED',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('k_amount', models.FloatField()),
                ('keyseed', models.CharField(max_length=256)),
                ('p_id', models.CharField(max_length=256)),
            ],
        ),
    ]
