# Generated by Django 5.1.1 on 2024-11-23 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0002_appuser_delete_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appuser',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
