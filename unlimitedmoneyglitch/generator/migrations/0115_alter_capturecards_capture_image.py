# Generated by Django 4.2.7 on 2024-05-27 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0114_alter_user_capture_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capturecards',
            name='capture_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]